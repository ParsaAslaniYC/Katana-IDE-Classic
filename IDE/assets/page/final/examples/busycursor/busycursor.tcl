#############################################################################
# Generated by SEEMAN version 7.4
#  in conjunction with Tcl version 8.6
#  Jul 31, 2022 07:44:48 PM +0430  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within SEEMAN."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 12"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {Nimbus Sans L} -size 14"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #45d84f
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #85d845
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
}



    vTcl::widgets::core::popup::createCmd .pop46 \
        -activebackground $vTcl(analog_color_m) -activeborderwidth 1 \
        -activeforeground black -background #45d84f -borderwidth 1 \
        -disabledforeground #b8a786 -font {-family {Nimbus Sans L} -size 14} \
        -foreground $vTcl(actual_gui_fg) -tearoff 1 
    global vTcl
    set val vTcl(.pop46,-proc)
    set vTcl(.pop46,-proc) popup1
    namespace eval ::widgets::.pop46 {}
    set ::widgets::.pop46::ClassOption(-proc) popup1
    set ::widgets::.pop46::options(-proc) popup1
    set ::widgets::.pop46::save(-proc) 1
    vTcl:DefineAlias ".pop46" "Popupmenu1" vTcl:WidgetProc "" 1
    .pop46 add cascade \
        -menu .pop46.men47 -label NewCascade 
    set site_2_0 "."
    menu .pop46.men47 \
        -activebackground #f4bcb2 -activeforeground #000000 \
        -background $vTcl(actual_gui_menu_bg) \
        -font $vTcl(actual_gui_font_menu_desc) \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    .pop46.men47 add command \
        -command {#} -label NewCommand 

proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
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
    wm geometry $top 600x450+660+210
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1905 1050
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Busy Cursor Example"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound none \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Run 
    vTcl:DefineAlias "$top.but46" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Quit 
    vTcl:DefineAlias "$top.but47" "Button2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but46 \
        -in $top -x 230 -y 150 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 240 -y 300 -anchor nw -bordermode ignore 
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
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

