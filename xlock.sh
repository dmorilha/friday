xlock -mode blank -geometry 1x1-1-1 &
A=$!
./friday.py &
B=$!
xrandr --output DVI1 --same-as VGA1
wait $A
xrandr --output VGA1 --right-of DVI1
kill $B;
