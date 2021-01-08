#Sets fish greeting to nothing, removes welcome message.
set fish_greeting
#checks if I logged in. If so, starts startx.
if status --is-login
	if test -z "$DISPLAY" -a $XDG_VTNR = 1
		exec startx
	end
end
# Opens my preferred prompt: starship
starship init fish | source
# Runs a custom pfetch script.
umutfetch
# start X at login
if status --is-login
	if test -z "$DISPLAY" -a $XDG_VTNR = 1
		exec startx
	end
end
