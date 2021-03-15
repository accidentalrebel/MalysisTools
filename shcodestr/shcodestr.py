import sys
import os

input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_filename, 'r', encoding='unicode_escape') as input_file:
        s = input_file.read().replace('\n', '')
        with open(output_filename, 'wb') as gen_file:
                gen_file.write(b'' + bytes(s, encoding='raw_unicode_escape'))

        input_file.close()
        gen_file.close()

        print('Done')
        os.system('cat ' + output_filename)
