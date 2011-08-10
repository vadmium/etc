/* See
http://kb.mozillazine.org/About:config_entries
http://preferential.mozdev.org/preferences.html
http://kb.mozillazine.org/Category:Preferences
*/

user_pref("kmeleon.toolband.Menu.size", 32767);
user_pref("kmeleon.toolband.&Main Bar.index", 1);
user_pref("kmeleon.toolband.&Main Bar.break", 0);
user_pref("kmeleon.toolband.&Zoom Buttons.index", 2);
user_pref("kmeleon.toolband.&Zoom Buttons.break", 1);
user_pref("kmeleon.toolband.&Search Buttons.index", 3);
user_pref("kmeleon.toolband.Mail/&News Buttons.visibility", false);
user_pref("kmeleon.toolband.URL Bar.index", 5);
user_pref("kmeleon.toolband.URL Bar.size", 32767);
user_pref("kmeleon.toolband.&Go Buttons.index", 6);
user_pref("kmeleon.toolband.Tab/&Window Buttons.index", 7);
user_pref("kmeleon.toolband.&Privacy Bar.break", 1);
user_pref("kmeleon.toolband.&Privacy Bar.visibility", true);

user_pref("kmeleon.plugins.bookmarks.openurl", "ID_OPEN_LINK_IN_NEW_TAB");
user_pref("kmeleon.plugins.macros.selected.openurl", "ID_OPEN_LINK_IN_NEW_TAB");
user_pref("kmeleon.tabs.onOpenOption", 1);
user_pref("browser.link.open_newwindow", 3);
user_pref("browser.link.open_newwindow.restriction", 0);

user_pref("kmeleon.plugins.gestures.up", "macros(Go_Up)");

user_pref("browser.startup.page", 0);

/* ==== Potential annoyances */

/* Disable blinking text */
// user_pref("browser.blink_allowed", false);

/* Image animation mode: normal, once, none. */
// user_pref("image.animation_mode", "once");

/* Show pref UI to block images that don't come from the current server */
// user_pref("imageblocker.enable", true);

/* Turn that annoying autocomplete popup REALLY off */
// user_pref("browser.urlbar.autocomplete.enabled", false);
// user_pref("browser.urlbar.showPopup", false);
// user_pref("browser.urlbar.showSearch", false);

/* Turn off the download manager (0=download manager, 1=simple dialog?) */
user_pref("browser.downloadmanager.behavior", 1);

/* Enable the marquee tag (disabled by default) */
user_pref("browser.display.enable_marquee", true);

/* ==== Platform/UI parity */

/* Key modifier stuff: see bug 22515 */
/* Motif style */
// user_pref("ui.key.accelKey", 18);
// user_pref("ui.key.menuAccessKey", 0);
//user_pref("ui.key.menuAccessKeyFocuses", false);

/* Windows style */
//user_pref("ui.key.accelKey", 17);
//user_pref("ui.key.menuAccessKey", 18);
//user_pref("ui.key.menuAccessKeyFocuses", true);

/* Unix-style autocopy */
//user_pref("clipboard.autocopy", false);

/* Middle mouse prefs: true by default on Unix, false on other platforms. */
// user_pref("middlemouse.paste", false);
user_pref("middlemouse.openNewWindow", true);
user_pref("middlemouse.contentLoadURL", false);
// user_pref("middlemouse.scrollbarPosition", false);

user_pref("general.autoScroll", true);

/* Newline paste behavior: 0 => paste unchanged; 1 => paste only first line;
2 => replace with spaces; 3 => strip newlines */
//user_pref("editor.singleLine.pasteNewlines", 0);

/* Bug in Netscape 6 branch: drag out of frame style pref was never
initialised on Unix, so dragging below a line of text doesn't snap selection
to the end of the line. */
//pref("browser.drag_out_of_frame_style", 1);

/* ==== UI */

/* Tab focus model bit field:
1 focuses text controls, 2 focuses other form elements, 4 adds links. */
// user_pref("accessibility.tabfocus", 1);

/* X font banning: see bug 104075. */
// user_pref("font.x11.rejectfontpattern", "fname=.*arial.*");

/* Some alternate forms for rejectfontpattern:
"fname=.*arial.*;scalable=.*;outline_scaled=.*;\
xdisplay=.*;xdpy=.*;ydpy=.*;xdevice=.*"
"fname=-zz-abiword.*;scalable=false;outline_scaled=false;" */

/* Alternately, reject font if accept pattern does not match it */
//user_pref("font.x11.acceptfontpattern", ".*");

/* Submenu delay */
/* Set it to be really long so that menus will stay posted until one clicks
somewhere, instead of un-posting whenever the mouse strays off the menu or
cuts across the border between a menu and a submenu */
user_pref("ui.submenuDelay", 7000);

/* Typeahead find configuration */
user_pref("accessibility.typeaheadfind", true);
user_pref("accessibility.typeaheadfind.linksonly", true);
user_pref("accessibility.typeaheadfind.startlinksonly", false);

/* Select colors for text */
// user_pref("ui.textSelectBackground", "green");
// user_pref("ui.textSelectForeground", "white");

/* Select color for typeahead find */
// user_pref("ui.textSelectBackgroundAttention", "blue");

/* Not clear when/if widgetSelectBackground ever gets called. */
// user_pref("ui.widgetSelectBackground", "orange");

/* ==== Popup windows */

/* Configurable security policies to override popups, see
http://www.mozilla.org/projects/security/components/ConfigPolicy.html */
// user_pref("capability.policy.popupsites.sites", "http://www.annoyingsite1.com http://www.popupsite2.com");
// user_pref("capability.policy.popupsites.Window.open","noAccess");

/* Turn it off everywhere */
// user_pref("capability.policy.default.Window.open","noAccess");

/* Disable JS windows popping up without direct action from the user */
user_pref("dom.disable_open_during_load", true);

/* Open links from external apps into a new tab */
// user_pref("browser.link.open_external", 3);

/* Force new windows into tabs */
user_pref("browser.link.open_newwindow", 3);

/* Make the above pref apply only to targeted links, not window.open */
// user_pref("browser.link.open_newwindow.restriction", 1);

/* Don't focus new tabs opened by left-click or external URL */
// user_pref("browser.tabs.loadDivertedInBackground", true);

/* Control focusing of new tabs opened by middle-click or ctrl-click */
// user_pref("browser.tabs.loadInBackground", false);

/* When the "dom.disable_open_click_delay" pref is set to a non-zero number,
"window.open" will fail when called more than that number of milliseconds
after a mouse click. */
// user_pref("dom.disable_open_click_delay", 1000);

/* ==== Miscellaneous stuff */

/* User-agent string */
// user_pref("general.useragent.override", "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.0.0; hi, Mom) Gecko/20020604");

/* Syntax highlighting in "View Source". */
// user_pref("browser.view_source.syntax_highlight", false);

/* In chatzilla, show original text in addition to smiley substitutions */
user_pref("extensions.irc.munger.smileyText", true);

/* Wrap column for html output from the editor */
// user_pref("editor.htmlWrapColumn", 72);

/* Show JS warnings. */
// user_pref("javascript.options.strict", true);

/* Default paper size */
user_pref("print.postscript.paper_size", "A4");

user_pref("browser.rights.3.shown", true);
user_pref("browser.xul.error_pages.expert_bad_cert", true);
user_pref("general.warnOnAboutConfig", false);

user_pref("font.name.serif.x-western", "Nimbus Roman No9 L");
user_pref("dom.disable_window_move_resize", true);

user_pref("browser.tabs.animate", false);

user_pref("font.name.sans-serif.x-western", "Nimbus Sans L");
user_pref("font.name.serif.x-western", "Nimbus Roman No9 L");
