I have not tried this yet, but plan to.



# Why can't I run GUI apps as root: "No protocol specified"?

I installed Debian onto my machine last night. Now, I don't understand why I can't run GUI apps from a terminal when running as root.

For example:

    sudo -i
    glxgears

Generates the following output:

    No protocol specified
    Error: couldn't open display :0

But when I first open the terminal I can run `glxgears` from the user account. It's only after I do `sudo -i` that the problem crops up.  This happens for any GUI app that I try to run.

I think it's probably related to X11, but I'm not sure.

-------------

Accessing the X server requires two things:

* The `$DISPLAY` variable pointing to the correct display (usually `:0`)
* Proper authentication information

The authentication information can be explicitly specified via `$XAUTHORITY`, and defaults to `~/.Xauthority` otherwise.

If `$DISPLAY` and `$XAUTHORITY` is set for your user, `sudo` will set them for the new shell, too, and everything should work fine.

If they are not set, they will probably default to the wrong values and you cannot start and X applications.

In Debian `$XAUTHORITY` is usually not set explicitly. Just add

    export XAUTHORITY=~/.Xauthority

to your `.bashrc` or explicitly say `XAUTHORITY=~/.Xauthority sudo ...` and everything should work.

You can also use `xauth list` to check whether proper authentication information are available.
