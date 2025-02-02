from ipykernel.kernelbase import Kernel
import os


WNames = open('/home/nicola/Gits/JWLS_2/JWLS_2_kernel/Names.wl.txt',
              'r').read().split()

######################################################################################
class JWLS_2_kernel(Kernel):
    
    implementation = 'JWLS_2'
    implementation_version = '2.0'
    language = 'Wolfram Language'
    language_info = {'name': 'WolframScript',
                     'codemirror_mode': 'mathematica',
                     'mimetype': 'text/x-mathematica',
                     'file_extension': '.wl'}
                     
    banner = "Jupyter for Wolfram Language Scripts"

    
    ##################################################################################
    def do_execute(self, code, silent, store_history=False, user_expressions=None,
                   allow_stdin=False):
        
        wl_response = os.popen('echo '+"'"+code+"'"+' | nc 127.0.0.1 5858').read()

        stream_content = {'name': 'stdout', 'text': wl_response}
        self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
               
    
    ##################################################################################
    def do_complete(self, code, cursor_pos):
        code = code[:cursor_pos]
        default = {'matches': [], 'cursor_start': 0,
                   'cursor_end': cursor_pos,
                   'status': 'ok'}
       
        if not code or code[-1] == ' ':
            return default
        
        token =  code.replace(';', ' ').replace('@', ' ').replace('/', ' '
                    ).replace('?', ' ').replace(',', ' ').replace('.', ' '
                    ).replace('>', ' ').replace('<', ' ').replace(':', ' '
                    ).replace('[', ' ').replace(']', ' ').replace('(', ' '
                    ).replace(')', ' ').replace('{', ' ').replace('}', ' '
                    ).replace('_', ' ').replace('+', ' ').replace('*', ' '
                    ).replace('#', ' ').replace('=', ' ').replace('"', ' '
                    ).replace('~', ' ').replace('&', ' ').replace('|', ' '
                    ).replace('!', ' ').split()[-1]
                            
        start = cursor_pos - len(token)

        matches = [m for m in WNames if m.startswith(token)]

        return {'matches': sorted(matches), 'cursor_start': start,
                'cursor_end': cursor_pos,
                'status': 'ok'}
