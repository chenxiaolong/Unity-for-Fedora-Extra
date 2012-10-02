/* Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to> */
/* License: GPLv3+ */

/* Compile with (gcc|clang) guest-account.c -lprocps */

/* GNU's basename() is more convenient */
#define _GNU_SOURCE

/* For nftw */
#define _XOPEN_SOURCE 500

#include <ctype.h>
#include <dirent.h>
#include <ftw.h>
#include <grp.h>
#include <proc/readproc.h>
#include <pwd.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mount.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int execute(char *program, char *arguments[]) {
  pid_t pid;
  int status;

  pid = fork();

  if (pid < 0) {
    fprintf(stderr, "fork() failed\n");
    exit(1);
  }
  else if (pid == 0) {
    if (execvp(program, arguments) < 0) {
      fprintf(stderr, "execvp() failed\n");
      exit(1);
    }
    exit(0);
  }
  else {
    waitpid(pid, &status, 0);
    return WEXITSTATUS(status);
  }
}

static int remove_callback(const char *fpath, const struct stat *sb,
                           int typeflag, struct FTW *ftwbuf) {
  int return_value = remove(fpath);
  if (return_value != 0) {
    fprintf(stderr, "Failed to remove %s\n", fpath);
  }
  return 0;
}

int recursively_remove(char *dpath) {
  return nftw(dpath, remove_callback, 20, FTW_DEPTH | FTW_MOUNT | FTW_PHYS);
}

int dir_exists_and_has_files(char *dpath) {
  struct stat info;
  if (stat(dpath, &info) == 0) {
    if (!S_ISDIR(info.st_mode)) {
      return -1;
    }

    DIR *dir_ptr = opendir(dpath);
    int files_count = 0;

    if (dir_ptr != NULL) {
      struct dirent *dir_entry = NULL;
      do {
        dir_entry = readdir(dir_ptr);
        if (dir_entry != NULL) {
          files_count++;
        }
      } while (dir_entry != NULL);
    }

    /* '.' and '..' */
    if (files_count == 2) {
      closedir(dir_ptr);
      return -1;
    }
  }
  else {
    return -1;
  }

  return 0;
}

int recursively_chown(char *dpath, uid_t user, gid_t group) {
  DIR *dir_ptr = opendir(dpath);
  int error = 0;

  if (dir_ptr != NULL) {
    struct dirent *dir_entry = NULL;
    do {
      dir_entry = readdir(dir_ptr);

      if (dir_entry != NULL) {
        /* Do not chown . or .. */
        if (strcmp(dir_entry->d_name, ".") == 0 ||
            strcmp(dir_entry->d_name, "..") == 0) {
          continue;
        }

        /* 1 ("/") + 1 ("\0") */
        char fullpath[2 + strlen(dpath) + strlen(dir_entry->d_name)];
        fullpath[0] = '\0';
        strcat(fullpath, dpath);
        strcat(fullpath, "/");
        strcat(fullpath, dir_entry->d_name);

        if (chown(fullpath, user, group) != 0) {
          error = -1;
        }
      }
    } while (dir_entry != NULL);
  }
  closedir(dir_ptr);
  return error;
}

char * get_value_from_file(char *fpath, char *search) {
  FILE *file_ptr = fopen(fpath, "r");

  if (file_ptr == NULL) {
    fprintf(stderr, "File %s does not exist\n", fpath);
    return NULL;
  }

  char buffer[80];
  char found_string[80];
  memset(buffer, 0, 80);

  short found = 0;

  while (found == 0 && fgets(buffer, 80, file_ptr) != NULL) {
    int location_buffer = 0;
    int location_search = 0;
    int matched = 0;

    while (location_search < strlen(search) && location_buffer < 80) {
      if(buffer[location_buffer] != search[location_search]) {
        if (matched == 1) {
          location_search = 0;
          matched = 0;
        }
        else {
          location_buffer++;
        }
      }
      else {
        location_buffer++;
        location_search++;
        matched = 1;
      }
      if (location_search == strlen(search)) {
        int location_found_string = 0;
        while (location_buffer < 80) {
          if (buffer[location_buffer] == ' ' ||
              buffer[location_buffer] == '\t' ||
              buffer[location_buffer] == '\n') {
            location_buffer++;
          }
          else {
            found_string[location_found_string] = buffer[location_buffer];
            location_found_string++;
            location_buffer++;
          }
        }
        found_string[location_found_string] = '\0';
        found = 1;
        break;
      }
    }

    memset(buffer, 0, 80);
  }

  fclose(file_ptr);

  if (found == 0) {
    return NULL;
  }

  return strdup(found_string);
}

void kill_all_procs_user(char *username) {
  proc_t **processes = readproctab(PROC_FILLUSR | PROC_FILLSTAT);
  int i = 0;
  while (processes[i] != NULL) {
    if (strcmp(processes[i]->euser, username) == 0) {
      kill(processes[i]->tid, SIGKILL);
    }
    i++;
  }
}

void kill_all_procs_group(char *group) {
  proc_t **processes = readproctab(PROC_FILLGRP | PROC_FILLSTAT);
  int i = 0;
  while (processes[i] != NULL) {
    if (strcmp(processes[i]->egroup, group) == 0) {
      kill(processes[i]->tgid, SIGKILL);
    }
    i++;
  }
}

void remove_remaining_files(char *username) {
  struct passwd *user_info = getpwnam(username);

  DIR *dir_ptr = opendir("/tmp");

  if (dir_ptr != NULL) {
    struct dirent *dir_entry = NULL;
    do {
      dir_entry = readdir(dir_ptr);
      if (dir_entry != NULL) {
        struct stat info;

        /* 4 ("/tmp") + 1 ("/") + 1 ("\0") */
        char fullpath[6 + strlen(dir_entry->d_name)];
        fullpath[0] = '\0';
        strcat(fullpath, "/tmp/");
        strcat(fullpath, dir_entry->d_name);

        if (stat(fullpath, &info) == 0 &&
            info.st_uid == user_info->pw_uid) {
          recursively_remove(fullpath);
        }
      }
    } while (dir_entry != NULL);
  }

  closedir(dir_ptr);
}

void run_scripts_in(char *dpath, char *username) {
  struct stat dirinfo;
  if (stat(dpath, &dirinfo) == 0) {
    if (!S_ISDIR(dirinfo.st_mode)) {
      fprintf(stderr, "%s is not a directory\n", dpath);
      return;
    }

    DIR *dir_ptr = opendir(dpath);

    if (dir_ptr != NULL) {
      struct dirent *dir_entry = NULL;
      do {
        dir_entry = readdir(dir_ptr);

        if (dir_entry != NULL) {
          /* 1 ("/") + 1 ("\0") */
          char fullpath[2 + strlen(dpath) + strlen(dir_entry->d_name)];
          fullpath[0] = '\0';
          strcat(fullpath, dpath);
          strcat(fullpath, "/");
          strcat(fullpath, dir_entry->d_name);

          struct stat info;
          stat(fullpath, &info);
          if (access(fullpath, X_OK) == 0 && !S_ISDIR(info.st_mode)) {
            char *args_su[] = {"/usr/bin/su", username, "-c",
                               fullpath, NULL};
            int exit_status = execute("/usr/bin/su", args_su);
            if (exit_status != 0) {
              fprintf(stderr, "%s exited with status %i\n", fullpath,
                      exit_status);
            }
          }
        }
      } while (dir_entry != NULL);
    }

    closedir(dir_ptr);
  }
  else {
    fprintf(stderr, "%s does not exist\n", dpath);
  }
}

void add_account() {
  char *home_directory;
  char *username;

  /* The TMPDIR environment variable has a higher priority than the first
   * argument in tempnam(), so we'll clear it */
  putenv("TMPDIR=");

  /* Find a unique name for the guest user's home directory and make sure that
   * the guest user doesn't already exist */
  do {
    home_directory = tempnam("/tmp", "guest");
    if (home_directory == NULL) {
      fprintf(stderr, "Failed to create unique directory name\n");
      exit(1);
    }

    /* useradd does not accept uppercase letters in the username */
    int i;
    for (i = 0; i < strlen(home_directory); i++) {
      home_directory[i] = tolower(home_directory[i]);
    }

    username = basename(home_directory);
  } while (access(home_directory, F_OK) == 0 && getpwnam(username) != NULL);

  /* Create user */
  char *args_useradd[] = {"/usr/sbin/useradd",
                          "--system",
                          "--no-create-home",
                          "--home-dir", "/",
                          "--comment", "Guest",
                          "--user-group",
                          "--shell", "/bin/bash",
                          username, NULL};
  int exit_code = execute("/usr/sbin/useradd", args_useradd);
  if (exit_code != 0) {
    umount(home_directory);
    recursively_remove(home_directory);
    fprintf(stderr, "Failed to create guest user: %s\n", username);
    exit(1);
  }

  /* Create temporary home directory */
  mkdir(home_directory, S_IRWXU);

  /* Mount home directory as tmpfs */
  if (mount("none", home_directory, "tmpfs", MS_NOSUID, "mode=700") != 0) {
    fprintf(stderr, "Failed to mount %s as tmpfs\n", home_directory);
    recursively_remove(home_directory);
    exit(1);
  }

  /* Take ownership of home directory */
  struct passwd *user_info = getpwnam(username);
  if (chown(home_directory, user_info->pw_uid, user_info->pw_gid) != 0) {
    fprintf(stderr, "Failed to take ownership of %s\n", home_directory);
    umount(home_directory);
    recursively_remove(home_directory);
  }

  /* Recursively copy skeleton files to home directory */
  if (dir_exists_and_has_files("/etc/guest-session/skel") == 0) {
    char *args_copy[] = {"/usr/bin/cp", "-rT", "/etc/guest-session/skel",
                         home_directory, NULL};
    execute("/usr/bin/cp", args_copy);
  }
  else {
    char *args_copy[] = {"/usr/bin/cp", "-rT", "/etc/skel", home_directory,
                         NULL};
    execute("/usr/bin/cp", args_copy);
  }

  /* Set the guest user's home directory */
  char *args_usermod[] = {"/usr/sbin/usermod", "-d", home_directory,
                          username, NULL};
  execute("/usr/sbin/usermod", args_usermod);

  /* Run any additional scripts */
  if (dir_exists_and_has_files("/etc/guest-session/post-add.d") == 0) {
    run_scripts_in("/etc/guest-session/post-add.d", username);
  }

  /* Take ownership of all the files in the guest user's home directory */
  if (recursively_chown(home_directory, user_info->pw_uid,
                        user_info->pw_gid) != 0) {
    fprintf(stderr, "Failed to chown all files\n");
  }

  /* Print to username so LightDM knows which user was created */
  printf("%s\n", username);
}

void remove_account(char *username) {
  struct passwd *user_info = getpwnam(username);

  if (user_info == NULL) {
    fprintf(stderr, "User %s does not exist\n", username);
    exit(1);
  }

  struct group *group_info = getgrgid(user_info->pw_gid);

  uid_t sys_uid_min, sys_uid_max;
  gid_t sys_gid_min, sys_gid_max;

  char *sys_uid_min_str = get_value_from_file("/etc/login.defs", "SYS_UID_MIN");
  char *sys_uid_max_str = get_value_from_file("/etc/login.defs", "SYS_UID_MAX");
  char *sys_gid_min_str = get_value_from_file("/etc/login.defs", "SYS_GID_MIN");
  char *sys_gid_max_str = get_value_from_file("/etc/login.defs", "SYS_GID_MAX");

  if (sys_uid_min_str == NULL) {
    fprintf(stderr, "SYS_UID_MIN not defined in /etc/login.defs\n");
    exit(1);
  }
  if (sys_uid_max_str == NULL) {
    fprintf(stderr, "SYS_UID_MAX not defined in /etc/login.defs\n");
    exit(1);
  }
  if (sys_gid_min_str == NULL) {
    fprintf(stderr, "SYS_GID_MIN not defined in /etc/login.defs\n");
    exit(1);
  }
  if (sys_gid_max_str == NULL) {
    fprintf(stderr, "SYS_GID_MAX not defined in /etc/login.defs\n");
    exit(1);
  }

  sys_uid_min = atoi(sys_uid_min_str);
  sys_uid_max = atoi(sys_uid_max_str);
  sys_gid_min = atoi(sys_gid_min_str);
  sys_gid_max = atoi(sys_gid_max_str);

  if (user_info->pw_uid < sys_uid_min ||
      user_info->pw_uid > sys_uid_max ||
      user_info->pw_gid < sys_gid_min ||
      user_info->pw_gid > sys_gid_max) {
    fprintf(stderr, "User %s is not a system user\n", username);
    exit(1);
  }

  if (strstr(user_info->pw_dir, "/tmp") == NULL) {
    fprintf(stderr, "Home directory %s is not in /tmp\n", user_info->pw_dir);
    exit(1);
  }

  /* Kill all of the users processes */
  kill_all_procs_user(username);
  kill_all_procs_group(group_info->gr_name);

  /* Unmount tmpfs */
  if (umount(user_info->pw_dir) != 0) {
    fprintf(stderr, "Failed to unmount %s\n", user_info->pw_dir);
    umount2(user_info->pw_dir, MNT_DETACH);
  }

  recursively_remove(user_info->pw_dir);

  /* Remove remaining files in /tmp owned by the guest user */
  remove_remaining_files(username);

  /* Delete user */
  char *args_userdel[] = {"/usr/sbin/userdel", username, NULL};
  if (execute("/usr/sbin/userdel", args_userdel) != 0) {
    fprintf(stderr, "Failed to create guest user: %s\n", username);
    exit(1);
  }

  /* Run any additional scripts */
  if (dir_exists_and_has_files("/etc/guest-session/post-remove.d") == 0) {
    run_scripts_in("/etc/guest-session/post-remove.d", username);
  }
}

int main(int argc, char *argv[]) {
  if (getuid() != 0) {
    fprintf(stderr, "guest-account must be run as root\n");
    exit(1);
  }

  if (argc < 2) {
    fprintf(stderr, "Usage: %s add|remove\n", argv[0]);
    exit(1);
  }
  if (strcmp(argv[1], "add") == 0) {
    add_account();
  }
  else if (strcmp(argv[1], "remove") == 0) {
    if (argc < 3) {
      fprintf(stderr, "Usage: %s remove [account]\n", argv[0]);
      exit(1);
    }
    remove_account(argv[2]);
  }
  else {
    fprintf(stderr, "Usage: %s add|remove\n", argv[0]);
    exit(1);
  }
}
