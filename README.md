This python script prints ARM extension for specific cpu features found in /proc/cpuinfo

Example output:
$ ./aarch64_cpu_info.py 
Detected CPU Features:
------------------------
aes, evtstrm, pmull, crc32, fphp, asimdrdm, lrcpc, sha2, atomics, fp, asimd, asimdhp, sha1, asimddp, dcpop, ssbs, cpuid

Supported ARMv Extensions:
---------------------------
ARMv8.0: aes, evtstrm, crc32, pmull, sha2, fp, asimd, sha1, ssbs, cpuid
ARMv8.1: atomics, asimdrdm
ARMv8.2: dcpop, asimdhp, fphp, asimddp
ARMv8.3: lrcpc

No unknown extensions found.
