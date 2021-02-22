nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceCompositionPipeline = On }"
xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output eDP-1-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1-1 --off
xinput set-prop "HUION Huion Tablet Pen stylus" "Coordinate Transformation Matrix" 0.5, 0, 0.5, 0, 1, 0, 0, 0, 1
xsetwacom --set "HUION Huion Tablet Pad pad" Button 3 "key +Print"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 2 "key control alt shift +F12"
xsetwacom --set "HUION Huion Tablet Pad pad" Button 1 "key control alt shift +F11"
xsetwacom --set "HUION Huion Tablet Pen stylus" Button 3 "key control +Z"
setxkbmap tr
picom --experimental-backends &
nitrogen --restore &
blueman-applet &
nm-applet &
flameshot &
clipit &
dunst &
searx-run &
exec qtile
