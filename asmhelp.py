#Tested over IDA 7.5 
import os, idaapi, idc, json, webbrowser

#Useful website with some info about x86 cmds
basic_url_asm_help = 'https://www.aldeid.com/wiki/X86-assembly/Instructions/'
asmcmds_aval_json = "path-to-asmcmds.json"
asmcmds_aval = []

def InitCmd():
    global asmcmds_aval_json, asmcmds_aval
    print("Loading ASM CMDs availables")
    if os.path.exists(asmcmds_aval_json):
        asmcmds_aval = json.load(open(asmcmds_aval_json))
    return

def ASmHelp():
    global basic_url_asm_help, asmcmds_aval
    name = idaapi.get_highlight(idaapi.get_current_viewer())
    if name and name[1] and name[0] in asmcmds_aval:
        webbrowser.open(f'{basic_url_asm_help}{name[0]}')

class AsmHelp_t(idaapi.plugin_t):
    comment = "ASM Helper"
    help = "ASM Helper shortcut key is Ctrl-,"
    wanted_name = "ASM Helper"
    wanted_hotkey = "Ctrl-,"
    flags = idaapi.PLUGIN_KEEP

    def init(self):
        print("ASM Helper loaded\n")
        InitCmd()
        return idaapi.PLUGIN_KEEP

    def term(self):
        print("ASM Helper terminated\n")

    def run(self, arg):
        ASmHelp()

def PLUGIN_ENTRY():
    return AsmHelp_t()
