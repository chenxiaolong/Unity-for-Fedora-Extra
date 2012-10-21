# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _ver_amazoncloudreader	2.2
%define _ver_angrybirds		2.2
%define _ver_bbcnews		2.2
%define _ver_cuttherope		2.2
%define _ver_facebookapps	2.2
%define _ver_facebookmessenger	2.2
%define _ver_gmail		2.4.7
%define _ver_googlecalendar	2.2
%define _ver_googledocs		2.2
%define _ver_googleplus		2.2
%define _ver_grooveshark	2.2
%define _ver_hulu_player	2.2
%define _ver_lastfm_radio	2.2
%define _ver_launchpad		2.2
%define _ver_librefm		2.2
%define _ver_linkedin		2.4.7
%define _ver_livemail		2.2
%define _ver_mail_ru		2.2
%define _ver_newsblur		2.2
%define _ver_pandora_com	2.2
%define _ver_qq_mail		2.2
%define _ver_reddit		2.2
%define _ver_tumblr		2.2
%define _ver_twitter		2.4.7
%define _ver_vkcom		2.2
%define _ver_wordpress_com	2.2
%define _ver_yahoomail		2.2
%define _ver_yahoonews		2.2
%define _ver_yandex_music	2.2
%define _ver_yandexnews		2.2
%define _ver_youtube		2.4.7

Name:		unity-webapps
Version:	1.0
Release:	3%{?dist}
Summary:	Metapackage for all the Unity WebApps

Group:		User Interface/Desktops
License:	GPLv3+
URL:		http://packages.ubuntu.com/search?keywords=webapps&searchon=names&suite=quantal&section=all

%define _base_url https://launchpad.net/ubuntu/+archive/primary/+files/unity-webapps

Source0:	%{_base_url}-amazoncloudreader_%{_ver_amazoncloudreader}.tar.gz
Source1:	%{_base_url}-angrybirds_%{_ver_angrybirds}.tar.gz
Source2:	%{_base_url}-bbcnews_%{_ver_bbcnews}.tar.gz
Source3:	%{_base_url}-cuttherope_%{_ver_cuttherope}.tar.gz
Source4:	%{_base_url}-facebookapps_%{_ver_facebookapps}.tar.gz
Source5:	%{_base_url}-facebookmessenger_%{_ver_facebookmessenger}.tar.gz
Source6:	%{_base_url}-gmail_%{_ver_gmail}.tar.gz
Source7:	%{_base_url}-googlecalendar_%{_ver_googlecalendar}.tar.gz
Source8:	%{_base_url}-googledocs_%{_ver_googledocs}.tar.gz
Source9:	%{_base_url}-googleplus_%{_ver_googleplus}.tar.gz
Source10:	%{_base_url}-grooveshark_%{_ver_grooveshark}.tar.gz
Source11:	%{_base_url}-hulu-player_%{_ver_hulu_player}.tar.gz
Source12:	%{_base_url}-lastfm-radio_%{_ver_lastfm_radio}.tar.gz
Source13:	%{_base_url}-launchpad_%{_ver_launchpad}.tar.gz
Source14:	%{_base_url}-librefm_%{_ver_librefm}.tar.gz
Source15:	%{_base_url}-linkedin_%{_ver_linkedin}.tar.gz
Source16:	%{_base_url}-livemail_%{_ver_livemail}.tar.gz
Source17:	%{_base_url}-mail-ru_%{_ver_mail_ru}.tar.gz
Source18:	%{_base_url}-newsblur_%{_ver_newsblur}.tar.gz
Source19:	%{_base_url}-pandora-com_%{_ver_pandora_com}.tar.gz
Source20:	%{_base_url}-qq-mail_%{_ver_qq_mail}.tar.gz
Source21:	%{_base_url}-reddit_%{_ver_reddit}.tar.gz
Source22:	%{_base_url}-tumblr_%{_ver_tumblr}.tar.gz
Source23:	%{_base_url}-twitter_%{_ver_twitter}.tar.gz
Source24:	%{_base_url}-vkcom_%{_ver_vkcom}.tar.gz
Source25:	%{_base_url}-wordpress-com_%{_ver_wordpress_com}.tar.gz
Source26:	%{_base_url}-yahoomail_%{_ver_yahoomail}.tar.gz
Source27:	%{_base_url}-yahoonews_%{_ver_yahoonews}.tar.gz
Source28:	%{_base_url}-yandex-music_%{_ver_yandex_music}.tar.gz
Source29:	%{_base_url}-yandexnews_%{_ver_yandexnews}.tar.gz
Source30:	%{_base_url}-youtube_%{_ver_youtube}.tar.gz

Requires:	unity-webapps-amazoncloudreader	= %{_ver_amazoncloudreader}
Requires:	unity-webapps-angrybirds	= %{_ver_angrybirds}
Requires:	unity-webapps-bbcnews		= %{_ver_bbcnews}
Requires:	unity-webapps-cuttherope	= %{_ver_cuttherope}
Requires:	unity-webapps-facebookapps	= %{_ver_facebookapps}
Requires:	unity-webapps-facebookmessenger	= %{_ver_facebookmessenger}
Requires:	unity-webapps-gmail		= %{_ver_gmail}
Requires:	unity-webapps-googlecalendar	= %{_ver_googlecalendar}
Requires:	unity-webapps-googledocs	= %{_ver_googledocs}
Requires:	unity-webapps-googleplus	= %{_ver_googleplus}
Requires:	unity-webapps-grooveshark	= %{_ver_grooveshark}
Requires:	unity-webapps-hulu-player	= %{_ver_hulu_player}
Requires:	unity-webapps-lastfm-radio	= %{_ver_lastfm_radio}
Requires:	unity-webapps-launchpad		= %{_ver_launchpad}
Requires:	unity-webapps-librefm		= %{_ver_librefm}
Requires:	unity-webapps-linkedin		= %{_ver_linkedin}
Requires:	unity-webapps-livemail		= %{_ver_livemail}
Requires:	unity-webapps-mail-ru		= %{_ver_mail_ru}
Requires:	unity-webapps-newsblur		= %{_ver_newsblur}
Requires:	unity-webapps-pandora-com	= %{_ver_pandora_com}
Requires:	unity-webapps-qq-mail		= %{_ver_qq_mail}
Requires:	unity-webapps-reddit		= %{_ver_reddit}
Requires:	unity-webapps-tumblr		= %{_ver_tumblr}
Requires:	unity-webapps-twitter		= %{_ver_twitter}
Requires:	unity-webapps-vkcom		= %{_ver_vkcom}
Requires:	unity-webapps-wordpress-com	= %{_ver_wordpress_com}
Requires:	unity-webapps-yahoomail		= %{_ver_yahoomail}
Requires:	unity-webapps-yahoonews		= %{_ver_yahoonews}
Requires:	unity-webapps-yandex-music	= %{_ver_yandex_music}
Requires:	unity-webapps-yandexnews	= %{_ver_yandexnews}
Requires:	unity-webapps-youtube		= %{_ver_youtube}

BuildArch:	noarch

%description
(no files)


%define webapp_package(n:N:v:u:)			\
%package %{-n*}						\
Summary:	Unity WebApp for %{*}			\
Group:		Applications/Internet			\
Version:	%{-v*}					\
License:	GPLv3 and Redistributable, no modification permitted	\
URL:		%{-u*}					\
Requires:	unity-webapps-common			\
Requires:	xdg-utils				\
BuildArch:	noarch					\
%description %{-n*}					\
This package contains the Unity WebApp for %{*}.

%webapp_package -n amazoncloudreader	-v %{_ver_amazoncloudreader}	-u https://read.amazon.com/		Amazon Cloud Reader
%webapp_package -n angrybirds		-v %{_ver_angrybirds}		-u http://chrome.angrybirds.com/	Angry Birds
%webapp_package -n bbcnews 		-v %{_ver_bbcnews}		-u http://www.bbc.co.uk/news/		BBC News
%webapp_package -n cuttherope		-v %{_ver_cuttherope}		-u http://www.cuttherope.ie/		Cut the Rope
%webapp_package -n facebookapps		-v %{_ver_facebookapps}		-u http://apps.facebook.com/		Facebook Apps
%webapp_package -n facebookmessenger	-v %{_ver_facebookmessenger}	-u https://www.facebook.com/		Facebook Messenger
%webapp_package -n gmail		-v %{_ver_gmail}		-u https://mail.google.com/		GMail
%webapp_package -n googlecalendar	-v %{_ver_googlecalendar}	-u https://www.google.com/calendar/render	Google Calendar
%webapp_package -n googledocs		-v %{_ver_googledocs}		-u https://docs.google.com/		Google Docs
%webapp_package -n googleplus		-v %{_ver_googleplus}		-u https://plus.google.com/		Google Plus
%webapp_package -n grooveshark		-v %{_ver_grooveshark}		-u http://grooveshark.com/		Grooveshark
%webapp_package -n hulu-player		-v %{_ver_hulu_player}		-u http://www.hulu.com/profile/queue	Hulu Player
%webapp_package -n lastfm-radio		-v %{_ver_lastfm_radio}		-u http://www.last.fm/			Last.fm Radio
%webapp_package -n launchpad		-v %{_ver_launchpad}		-u https://launchpad.net/		Launchpad
%webapp_package -n librefm		-v %{_ver_librefm}		-u http://libre.fm/			Libre.fm
%webapp_package -n linkedin		-v %{_ver_linkedin}		-u http://www.linkedin.com/		LinkedIn
%webapp_package -n livemail		-v %{_ver_livemail}		-u http://mail.live.com/		Windows Live Mail
%webapp_package -n mail-ru		-v %{_ver_mail_ru}		-u http://mail.ru/			Mail.Ru
%webapp_package -n newsblur		-v %{_ver_newsblur}		-u http://newsblur.com/			NewsBlur
%webapp_package -n pandora-com		-v %{_ver_pandora_com}		-u http://www.pandora.com/		Pandora
%webapp_package -n qq-mail		-v %{_ver_qq_mail}		-u http://mail.qq.com/			QQ 邮箱
%webapp_package -n reddit		-v %{_ver_reddit}		-u http://www.reddit.com/		reddit
%webapp_package -n tumblr		-v %{_ver_tumblr}		-u https://www.tumblr.com/		Tumblr
%webapp_package -n twitter		-v %{_ver_twitter}		-u https://twitter.com/			Twitter
%webapp_package -n vkcom		-v %{_ver_vkcom}		-u http://vk.com/			VK
%webapp_package -n wordpress-com	-v %{_ver_wordpress_com}	-u https://wordpress.com/wp-admin/	WordPress
%webapp_package -n yahoomail		-v %{_ver_yahoomail}		-u https://mail.yahoo.com/		Yahoo! Mail
%webapp_package -n yahoonews		-v %{_ver_yahoonews}		-u http://news.yahoo.com/		Yahoo! News
%webapp_package -n yandex-music		-v %{_ver_yandex_music}		-u http://music.yandex.ru/		Яндекс.Музыка
%webapp_package -n yandexnews		-v %{_ver_yandexnews}		-u http://news.yandex.ru/		Яндекс.Новости
%webapp_package -n youtube		-v %{_ver_youtube}		-u http://www.youtube.com/		YouTube

%define webapp_add_doc(n:v:)					\
%doc unity-webapps-%{-n*}-%{-v*}/COPYING

%define webapp_add_data(n:)					\
%{_datadir}/unity-webapps/userscripts/unity-webapps-%{-n*}/

%define webapp_add_icons(n:)					\
%dir %{_datadir}/icons/hicolor/*/				\
%dir %{_datadir}/icons/hicolor/*/apps/				\
%dir %{_datadir}/icons/unity-webapps-applications/		\
%dir %{_datadir}/icons/unity-webapps-applications/*/		\
%dir %{_datadir}/icons/unity-webapps-applications/*/apps/	\
%{_datadir}/icons/hicolor/*/apps/%{-n*}				\
%{_datadir}/icons/unity-webapps-applications/*/apps/%{-n*}

%define icon_cache_scriptlets(n:)				\
%post %{-n*}							\
touch --no-create %{_datadir}/icons/hicolor/ &>/dev/null || :	\
%postun %{-n*}							\
if [ ${1} -eq 0 ]; then						\
  touch --no-create %{_datadir}/icons/hicolor/ &>/dev/null	\
  gtk-update-icon-cache -f %{_datadir}/icons/hicolor/ &>/dev/null || :	\
fi								\
%posttrans %{-n*}						\
gtk-update-icon-cache -f %{_datadir}/icons/hicolor/ &>/dev/null || : \

%files amazoncloudreader
%webapp_add_doc		-n amazoncloudreader	-v %{_ver_amazoncloudreader}
%webapp_add_data	-n amazoncloudreader
%files angrybirds
%webapp_add_doc		-n angrybirds		-v %{_ver_angrybirds}
%webapp_add_data	-n angrybirds
%webapp_add_icons	-n unity-webapps-angry-birds.png
%icon_cache_scriptlets	-n angrybirds
%files bbcnews
%webapp_add_doc		-n bbcnews		-v %{_ver_bbcnews}
%webapp_add_data	-n bbcnews
%webapp_add_icons	-n unity-webapps-bbc.png
%icon_cache_scriptlets	-n bbcnews
%files cuttherope
%webapp_add_doc		-n cuttherope		-v %{_ver_cuttherope}
%webapp_add_data	-n cuttherope
%webapp_add_icons	-n unity-webapps-cut-the-rope.png
%icon_cache_scriptlets	-n cuttherope
%files facebookapps
%webapp_add_doc		-n facebookapps		-v %{_ver_facebookapps}
%webapp_add_data	-n facebookapps
%files facebookmessenger
%webapp_add_doc		-n facebookmessenger	-v %{_ver_facebookmessenger}
%webapp_add_data	-n facebookmessenger
%webapp_add_icons	-n unity-webapps-facebook.png
%icon_cache_scriptlets	-n facebookmessenger
%files gmail
%webapp_add_doc		-n gmail		-v %{_ver_gmail}
%webapp_add_data	-n gmail
%webapp_add_icons	-n unity-webapps-gmail.png
%icon_cache_scriptlets	-n gmail
%files googlecalendar
%webapp_add_doc		-n googlecalendar	-v %{_ver_googlecalendar}
%webapp_add_data	-n googlecalendar
%webapp_add_icons	-n unity-webapps-google-calendar.png
%icon_cache_scriptlets	-n googlecalendar
%files googledocs
%webapp_add_doc		-n googledocs		-v %{_ver_googledocs}
%webapp_add_data	-n googledocs
%files googleplus
%webapp_add_doc		-n googleplus		-v %{_ver_googleplus}
%webapp_add_data	-n googleplus
%webapp_add_icons	-n unity-webapps-google-plus.png
%icon_cache_scriptlets	-n googleplus
%files grooveshark
%webapp_add_doc		-n grooveshark		-v %{_ver_grooveshark}
%webapp_add_data	-n grooveshark
%webapp_add_icons	-n unity-webapps-grooveshark.png
%icon_cache_scriptlets	-n grooveshark
%files hulu-player
%webapp_add_doc		-n hulu-player		-v %{_ver_hulu_player}
%webapp_add_data	-n hulu-player
%webapp_add_icons	-n unity-webapps-hulu.png
%icon_cache_scriptlets	-n hulu-player
%files lastfm-radio
%webapp_add_doc		-n lastfm-radio		-v %{_ver_lastfm_radio}
%webapp_add_data	-n lastfm-radio
%webapp_add_icons	-n unity-webapps-last-fm.png
%icon_cache_scriptlets	-n lastfm-radio
%files launchpad
%webapp_add_doc		-n launchpad		-v %{_ver_launchpad}
%webapp_add_data	-n launchpad
%webapp_add_icons	-n unity-webapps-launchpad.png
%icon_cache_scriptlets	-n launchpad
%files librefm
%webapp_add_doc		-n librefm		-v %{_ver_librefm}
%webapp_add_data	-n librefm
%files linkedin
%webapp_add_doc		-n linkedin		-v %{_ver_linkedin}
%webapp_add_data	-n linkedin
%webapp_add_icons	-n unity-webapps-linkedin.png
%icon_cache_scriptlets	-n linkedin
%files livemail
%webapp_add_doc		-n livemail		-v %{_ver_livemail}
%webapp_add_data	-n livemail
%webapp_add_icons	-n unity-webapps-hotmail.png
%icon_cache_scriptlets	-n livemail
%files mail-ru
%webapp_add_doc		-n mail-ru		-v %{_ver_mail_ru}
%webapp_add_data	-n mail-ru
%webapp_add_icons	-n unity-webapps-mail-ru.png
%icon_cache_scriptlets	-n mail-ru
%files newsblur
%webapp_add_doc		-n newsblur		-v %{_ver_newsblur}
%webapp_add_data	-n newsblur
%webapp_add_icons	-n unity-webapps-newsblur.png
%icon_cache_scriptlets	-n newsblur
%files pandora-com
%webapp_add_doc		-n pandora-com		-v %{_ver_pandora_com}
%webapp_add_data	-n pandora-com
%files qq-mail
%webapp_add_doc		-n qq-mail		-v %{_ver_qq_mail}
%webapp_add_data	-n qq-mail
%webapp_add_icons	-n unity-webapps-mail-qq-com.png
%icon_cache_scriptlets	-n qq-mail
%files reddit
%webapp_add_doc		-n reddit		-v %{_ver_reddit}
%webapp_add_data	-n reddit
%webapp_add_icons	-n unity-webapps-reddit.png
%icon_cache_scriptlets	-n reddit
%files tumblr
%webapp_add_doc		-n tumblr		-v %{_ver_tumblr}
%webapp_add_data	-n tumblr
%files twitter
%webapp_add_doc		-n twitter		-v %{_ver_twitter}
%webapp_add_data	-n twitter
%webapp_add_icons	-n unity-webapps-twitter.png
%icon_cache_scriptlets	-n twitter
%files vkcom
%webapp_add_doc		-n vkcom		-v %{_ver_vkcom}
%webapp_add_data	-n vkcom
%webapp_add_icons	-n unity-webapps-vkontakte-ru.png
%icon_cache_scriptlets	-n vkcom
%files wordpress-com
%webapp_add_doc		-n wordpress-com	-v %{_ver_wordpress_com}
%webapp_add_data	-n wordpress-com
%webapp_add_icons	-n unity-webapps-wordpress.png
%icon_cache_scriptlets	-n wordpress-com
%files yahoomail
%webapp_add_doc		-n yahoomail		-v %{_ver_yahoomail}
%webapp_add_data	-n yahoomail
%webapp_add_icons	-n unity-webapps-yahoo-mail.png
%icon_cache_scriptlets	-n yahoomail
%files yahoonews
%webapp_add_doc		-n yahoonews		-v %{_ver_yahoonews}
%webapp_add_data	-n yahoonews
%webapp_add_icons	-n unity-webapps-yahoo-news.png
%icon_cache_scriptlets	-n yahoonews
%files yandex-music
%webapp_add_doc		-n yandex-music		-v %{_ver_yandex_music}
%webapp_add_data	-n yandex-music
%webapp_add_icons	-n unity-webapps-yandex-music.png
%icon_cache_scriptlets	-n yandex-music
%files yandexnews
%webapp_add_doc		-n yandexnews		-v %{_ver_yandexnews}
%webapp_add_data	-n yandexnews
%webapp_add_icons	-n unity-webapps-yandex-news.png
%icon_cache_scriptlets	-n yandexnews
%files youtube
%webapp_add_doc		-n youtube		-v %{_ver_youtube}
%webapp_add_data	-n youtube
%webapp_add_icons	-n unity-webapps-youtube.png
%icon_cache_scriptlets	-n youtube


%prep
%setup -q -T -c -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30


%install
for i in %{sources}; do
  DIR=$(echo ${i} | sed -n 's/^.*\/\(.*\)_\(.*\)\.tar.*$/\1-\2/p')
  pushd ${DIR}

  cat debian/install | while read SOURCE DEST; do
    if [ -f ${SOURCE} ]; then
      install -dm755 $RPM_BUILD_ROOT/${DEST}/
      install -m644 ${SOURCE} $RPM_BUILD_ROOT/${DEST}/
    elif [ -d ${SOURCE} ]; then
      pushd $RPM_BUILD_ROOT/${DEST}/
      find . -type d -exec install -dm755 $RPM_BUILD_ROOT/${DEST}/$(basename ${SOURCE})/{} \;
      find . -type f -exec install -m644 {} $RPM_BUILD_ROOT/${DEST}/$(basename ${SOURCE})/{} \;
      popd
    else
      echo "${SOURCE} does not exist!"
      exit 1
    fi
  done

  popd
done


%changelog
* Sat Oct 20 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-3
- Removed unity-webapps-googleplusgames (LP: 1065745)

* Sat Oct 06 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-2
- Accidentally put the Angry Birds icons in the Amazon Cloud Reader WebApp

* Fri Oct 05 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-1
- Initial release
- Look at the git history for more details on the updates
  - https://github.com/chenxiaolong/Unity-for-Fedora.git
