#!/usr/bin/python3
import os, subprocess, shutil

os.system("cp /localdisk/data/BPSM/Lecture11/plain_genomic_seq.txt . ")
os.listdir()

print("\n".join(os.listdir()))

print(open("plain_genomic_seq.txt").read())
print(open("plain_genomic_seq.txt").read().rstrip())

local_seq = open("plain_genomic_seq.txt").read().rstrip()
local_seq

import subprocess
subprocess.call("esearch -db nucleotide -query \"AJ223353[accession]\" | efetch -format fasta | grep -v \">\" > AJ223353_noheader.fasta3",shell=True)

remotefile = open("AJ223353_noheader.fasta3").read().upper()
remotefile
len(remotefile)

local_seq = open("plain_genomic_seq.txt").read().upper()
len(local_seq.rstrip())

remotefile_singleline = remotefile.replace("\n","")
remotefile_singleline_ready = remotefile_singleline
len(remotefile_singleline_ready)

local_seq_singleline = local_seq.replace("\n","")
len(local_seq_singleline)

remotefile_singleline_anythingleft = remotefile_singleline.replace("G","").replace("A","").replace("T","").replace("C","")
remotefile_singleline_anythingleft

local_seq_singleline_anythingleft = local_seq_singleline.replace("G","").replace("A","").replace("T","").replace("C","")
local_seq_singleline_anythingleft

local_seq_singleline_reallyDNA = local_seq_singleline.replace("X","").replace("S","").replace("K","").replace("L","")
local_seq_singleline_reallyDNA

set(list(local_seq.rstrip()))

len(local_seq_singleline_reallyDNA)

len(local_seq_singleline)

local_seq_singleline_ready = local_seq_singleline_reallyDNA

remote_noncoding01 = remotefile_singleline_ready[0:28]
remote_exon01 = remotefile_singleline_ready[28:409]
remote_noncoding02 = remotefile_singleline_ready[409:]

remote_noncoding01
remote_exon01
remote_noncoding02

local_exon01 = local_seq_singleline_ready[0:63]
local_intron01 = local_seq_singleline_ready[63:90]
local_exon02 = local_seq_singleline_ready[90:]


remote_exon01_out = open("remote_exon01.fasta", "w")
remote_exon01_out.write(">AJ223353_exon01_length" + str(len(remote_exon01)) + "\n")
remote_exon01_out.write(remote_exon01)
remote_exon01_out.close()
print(open("remote_exon01.fasta").read())
