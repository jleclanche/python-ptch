#!/usr/bin/env python
from ptch import PatchFile


def main():
	f = open("Achievement.dbc.ptch", "rb")
	ptch = PatchFile(f)
	print(ptch)

	out = open("Achievement.dbc.test", "wb")
	out.write(ptch.rleUnpack())
	out.close()


if __name__ == "__main__":
	main()
