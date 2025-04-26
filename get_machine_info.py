import os, tokenize
import platform
gPlatform = platform.machine()

def main():
    cwd = os.getcwd()
    src_path = os.path.join(cwd, 'uhf_host_peripheral','models','machineinfo.py')
    # print('src_path:',src_path)
    str_package = ''
    package_tokens = []
    with tokenize.open(src_path) as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            #print(token)
            if token.type != 3:
                continue
            if 'package' in token.line:
                if 'package' in token.string or \
                    '_package_' in token.line:
                    continue
                if 'self.software_info' in token.line:
                    continue
                package_tokens.append(token.string.strip())
    if len(package_tokens) == 1:
        str_package = package_tokens[0].replace("'",'')
        str_package = str_package.replace('.','-')
    if gPlatform != 'x86_64':
        str_package = '%s-%s'%(str_package,gPlatform)
    print(str_package)

if __name__ == '__main__':
    main()