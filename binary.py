#!/usr/bin/env python
# coding=utf-8
def intTobinary(paras):
    ### This is a int to binary paogram,it can translates int to binary.
    string=''
    try:
        var = hex(int(paras))
        s = str(var)
        for i in range(2,len(s)):
            if s[i]=='0':
                string+='0000 '
            if s[i]=='1':
                string+='0001 '
            if s[i]=='2':
                string+='0010 '
            if s[i]=='3':
                string+='0011 '
            if s[i]=='4':
                string+='0100 '
            if s[i]=='5':
                string+='0101 '
            if s[i]=='6':
                string+='0110 '
            if s[i]=='7':
                string+='0111 '
            if s[i]=='8':
                string+='1000 '
            if s[i]=='9':
                string+='1001 '
            if (s[i]=='a' or s[i]=='A'):
                string+='1010 '
            if (s[i]=='b' or s[i]=='B'):
                string+='1011 '
            if (s[i]=='c' or s[i]=='C'):
                string+='1100 '
            if (s[i]=='d' or s[i]=='D'):
                string+='1101 '
            if (s[i]=='e' or s[i]=='E'):
                string+='1110 '
            if (s[i]=='f' or s[i]=='F'):
                string+='1111 '
    except ValueError:
        print 'input is error: ',paras
#    print string
    return string

