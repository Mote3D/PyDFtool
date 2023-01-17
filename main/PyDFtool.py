#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__ = "Copyright (C) 2023 Henning Richter"
__email__ = "mote3d@quantentunnel.de"
__version__ = "1.0"
__license__ = """
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""



import sys
from tika import parser


def parse_file(fname):
    """Read and assign file content"""
    try:
        f = parser.from_file(fname, xmlContent=True)
    except FileNotFoundError:
        print("\nFile {} not found.\n".format(fname))
        sys.exit()

    # Split file content:
    plist = []
    ptext = {}
    strlength = len('<div class="page">')
    fcontent = f['content']

    for index, text in enumerate(fcontent):
        if fcontent[index:index+strlength] == '<div class="page">':
            plist.append(index)
            print(index, text)
        else:
            pass

    if plist:
        ptext.update({'header': fcontent[0:plist[0]]})
        if len(plist) > 1:
            if int(f['metadata']['xmpTPg:NPages']) == len(plist):
                pcounter = 1
                for i in range(1, len(plist), 1):
                    print(i)
                    ptext.update({'page'+str(pcounter): fcontent[plist[i-1]:plist[i]]})
                    pcounter += 1
                ptext.update({'page'+str(pcounter): fcontent[plist[i]:]})
            else:
                print("\nError reading file {}.\n".format(fname))
                sys.exit()
    return ptext



# Compare files:
def compare_content(pdictlist):
    """Compare content of two files"""
    if pdictlist[0].keys() == pdictlist[1].keys():
        print('comparing files...')
    else:
        pass



def main():

    filename1 = 'A.pdf'
    filename2 = 'B.pdf'


    # Read element variable output from .dat file:
    pagetext1 = parse_file(filename1)
    pagetext2 = parse_file(filename2)
    
    pagedictlist = [pagetext1, pagetext2]

    compare_content(pagedictlist)

    print(set(pagetext1.items()) ^ set(pagetext2.items()))


if __name__ == "__main__":
    main()
    
