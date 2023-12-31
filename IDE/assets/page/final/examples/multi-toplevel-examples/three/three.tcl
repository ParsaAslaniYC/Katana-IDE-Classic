#############################################################################
# Generated by SEEMAN version 7.4j
#  in conjunction with Tcl version 8.6
#  Apr 10, 2022 08:26:09 AM PDT  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within SEEMAN."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 14"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #f4bcb2
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) wheat
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #f4bcb2
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    vTcl::widgets::core::popup::createCmd .pop46 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font {-family {DejaVu Sans} -size 12} \
        -foreground $vTcl(actual_gui_fg) -tearoff 1 
    global vTcl
    set val vTcl(.pop46,-proc)
    set vTcl(.pop46,-proc) popup1
    namespace eval ::widgets::.pop46 {}
    set ::widgets::.pop46::ClassOption(-proc) popup1
    set ::widgets::.pop46::options(-proc) popup1
    set ::widgets::.pop46::save(-proc) 1
    vTcl:DefineAlias ".pop46" "Popupmenu1" vTcl:WidgetProc "" 1
    .pop46 add command \
        -command {#} -label This 
    .pop46 add command \
        -command {#} -label That 
    .pop46 add separator \
        
    .pop46 add cascade \
        -menu .pop46.men48 -command {{}} -label Also 
    set site_2_0 "."
    menu .pop46.men48 \
        -activebackground #f4bcb2 -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) \
        -font $vTcl(actual_gui_font_menu_desc) \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    .pop46.men48 add command \
        -command {#} -label Then 
    .pop46.men48 add command \
        -command {#} -label There 
    vTcl::widgets::core::popup::createCmd .pop47 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font {-family {DejaVu Sans} -size 12} \
        -foreground $vTcl(actual_gui_fg) -tearoff 1 
    global vTcl
    set val vTcl(.pop47,-proc)
    set vTcl(.pop47,-proc) popup2
    namespace eval ::widgets::.pop47 {}
    set ::widgets::.pop47::ClassOption(-proc) popup2
    set ::widgets::.pop47::options(-proc) popup2
    set ::widgets::.pop47::save(-proc) 1
    vTcl:DefineAlias ".pop47" "Popupmenu2" vTcl:WidgetProc "" 1
    .pop47 add command \
        -command {#} -label How 
    .pop47 add command \
        -command {#} -label Now 
    .pop47 add cascade \
        -menu .pop47.men49 -command {{}} -label {Brown Cow} 
    set site_2_0 "."
    menu .pop47.men49 \
        -activebackground #f4bcb2 -activeforeground black \
        -background $vTcl(actual_gui_menu_bg) \
        -font $vTcl(actual_gui_font_menu_desc) \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    .pop47.men49 add command \
        -command {#} -label Mo 

proc vTclWindow.top34 {base} {
    global vTcl
    if {$base == ""} {
        set base .top34
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 410x347+278+339
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Main"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Main" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but35 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command open_middle \
        -disabledforeground #b8a786 -font {-family {DejaVu Sans} -size 14} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Open Middle} 
    vTcl:DefineAlias "$top.but35" "Button1" vTcl:WidgetProc "Main" 1
    button $top.but36 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font {-family {DejaVu Sans} -size 14} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Quit 
    vTcl:DefineAlias "$top.but36" "Button2" vTcl:WidgetProc "Main" 1
    message $top.mes43 \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans Mono} -size 14} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Main GUI} -width 90 
    vTcl:DefineAlias "$top.mes43" "Message1" vTcl:WidgetProc "Main" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but35 \
        -in $top -x 0 -relx 0.317 -y 0 -rely 0.461 -anchor nw \
        -bordermode ignore 
    place $top.but36 \
        -in $top -x 0 -relx 0.4171 -y 0 -rely 0.692 -anchor nw \
        -bordermode ignore 
    place $top.mes43 \
        -in $top -x 0 -relx 0.361 -y 0 -rely 0.173 -width 0 -relwidth 0.237 \
        -height 0 -relheight 0.092 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top35 {base} {
    global vTcl
    if {$base == ""} {
        set base .top35
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 459x315+700+341
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Man in the Middle"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Middle" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    message $top.mes44 \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 12} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {This is a man-in-the-middle toplevel.

It is invoked from the main toplevel
and in turn invokes another GUI which
has a popup and therefore, needs "root".} \
        -width 326 
    vTcl:DefineAlias "$top.mes44" "Message1_1" vTcl:WidgetProc "Middle" 1
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command invoke \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Invoke 
    vTcl:DefineAlias "$top.but46" "Button1_1" vTcl:WidgetProc "Middle" 1
    button $top.but43 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Quit 
    vTcl:DefineAlias "$top.but43" "Button2_1" vTcl:WidgetProc "Middle" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.mes44 \
        -in $top -x 0 -relx 0.1438 -y 0 -rely 0.159 -width 0 -relwidth 0.71 \
        -height 0 -relheight 0.371 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 0 -relx 0.196 -y 0 -rely 0.698 -width 94 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but43 \
        -in $top -x 0 -relx 0.627 -y 0 -rely 0.698 -width 72 -relwidth 0 \
        -height 32 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top36 {base} {
    global vTcl
    if {$base == ""} {
        set base .top36
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 420x325+1171+339
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Popup"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Popup" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but37 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Button1 
    vTcl:DefineAlias "$top.but37" "Button1_2" vTcl:WidgetProc "Popup" 1
    bind $top.but37 <Button-3> {
        lambda e: popup1(e)
    }
    button $top.but38 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #b8a786 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Button2 
    vTcl:DefineAlias "$top.but38" "Button2_2" vTcl:WidgetProc "Popup" 1
    bind $top.but38 <Button-3> {
        lambda e: popup2(e)
    }
    message $top.mes43 \
        -background $vTcl(actual_gui_bg) \
        -font {-family {DejaVu Sans} -size 12} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Each button
has a popup menu.} -width 207 
    vTcl:DefineAlias "$top.mes43" "Message1_2" vTcl:WidgetProc "Popup" 1
    button $top.but44 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Quit 
    vTcl:DefineAlias "$top.but44" "Button3_1" vTcl:WidgetProc "Popup" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but37 \
        -in $top -x 0 -relx 0.168 -y 0 -rely 0.493 -width 91 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but38 \
        -in $top -x 0 -relx 0.524 -y 0 -rely 0.492 -width 91 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $top.mes43 \
        -in $top -x 0 -relx 0.2524 -y 0 -rely 0.092 -width 0 -relwidth 0.493 \
        -height 0 -relheight 0.28 -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 0 -relx 0.364 -y 0 -rely 0.783 -height 0 -relheight 0.152 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top34 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
set btop2 ""
if {$vTcl(borrow)} {
    set btop2 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop2 $vTcl(tops)] != -1} {
        set btop2 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop2
Window show .top35 $btop2
if {$vTcl(borrow)} {
    $btop2 configure -background plum
}
set btop3 ""
if {$vTcl(borrow)} {
    set btop3 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop3 $vTcl(tops)] != -1} {
        set btop3 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop3
Window show .top36 $btop3
if {$vTcl(borrow)} {
    $btop3 configure -background plum
}

