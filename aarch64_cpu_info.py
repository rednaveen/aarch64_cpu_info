#!/bin/python3
import re

#Reference links:
# * https://gpages.juszkiewicz.com.pl/arm-socs-table/arm-socs.html
# Thanks to author of above blog.

# Dictionary mapping ARMv extensions to their features
armv_extensions = {
    "ARMv8.1": ["asimdrdm", "atomics"],
    "ARMv8.0": ["fp", "asimd", "evtstrm", "cpuid", "aes", "crc32", "pmull", "sha1", "sha2","ssbs","sb","dgh"],
    "ARMv8.2": ["asimddp", "asimdfhm", "asimdhp", "bf16", "dcpodp", "dcpop", "flagm", "fphp", "i8mm", "sha3", "sha512", "sm3", "sm4", "sve", "svebf16", "svef32mm", "svef64mm", "svei8mm", "uscat","jscvt"],
    "ARMv8.3": ["fcma", "jsvt", "lrcpc"],
    "ARMv8.4": ["dit", "ilrcpc", "paca", "pacg"],
    "ARMv8.5": ["bti", "flagm2", "frint", "mte", "mte3", "rng"],
    "ARMv8.6": ["ecv"],
    "ARMv8.7": ["afp", "rpres", "wfxt"],
    "ARMv9.0": ["sve2", "sveaes", "svebitperm", "svepmull", "svesh3", "svesm4","svesha3"],
    "ARMv9.2": ["ebf16", "sme", "smeb16f32", "smef16f32", "smef32f32", "smef64f64", "smefa64", "smei8i32", "smei16i64", "sveebf16"]
}

# Dictionary mapping Neoverse processors to their features
neoverse_processors = {
    "Neoverse N1": ["sve", "svebf16", "svef32mm", "svef64mm", "svei8mm"],
    "Neoverse E1": [ "mte"],
    "Neoverse V1": ["sve2", "sveaes", "svebitperm", "svepmull", "svesh3", "svesm4"],
}

def parse_cpuinfo():
    """Parse /proc/cpuinfo and return a set of features."""
    features = set()
    with open("/proc/cpuinfo", "r") as f:
        for line in f:
            match = re.match(r"Features\s*:\s*(.*)", line)
            if match:
                features.update(match.group(1).split())
    return features

def find_armv_extensions(features):
    """Find ARMv extensions supported by the given features."""
    supported_extensions = {}
    for armv, armv_features in armv_extensions.items():
        common_features = set(armv_features) & features
        if common_features:
            supported_extensions[armv] = common_features
    return supported_extensions

def find_neoverse_processors(features):
    """Find Neoverse processors supported by the given features."""
    supported_processors = {}
    for processor, processor_features in neoverse_processors.items():
        common_features = set(processor_features) & features
        if common_features:
            supported_processors[processor] = common_features
    return supported_processors

def find_unknown_extensions(features):
    """Find features that are not in the armv_extensions or neoverse_processors dictionaries."""
    known_features = set()
    for armv_features in armv_extensions.values():
        known_features.update(armv_features)
    for processor_features in neoverse_processors.values():
        known_features.update(processor_features)
    
    unknown_extensions = features - known_features
    return unknown_extensions

def main():
    features = parse_cpuinfo()
    supported_extensions = find_armv_extensions(features)
    supported_processors = find_neoverse_processors(features)
    unknown_extensions = find_unknown_extensions(features)
    
    print("Detected CPU Features:")
    print("------------------------")
    print(", ".join(features))
    print()
    
    print("Supported ARMv Extensions:")
    print("---------------------------")
    for armv, features in supported_extensions.items():
        print(f"{armv}: {', '.join(features)}")
    print()

    print("Detected CPU Features by Neoverse:")
    print("----------------------------------")
    for armv, features in supported_processors.items():
        print(f"{armv}: {', '.join(features)}")
    print()

    if unknown_extensions:
        print("Unknown Extensions:")
        print("-------------------")
        print(", ".join(unknown_extensions))
    else:
        print("No unknown extensions found.")

if __name__ == "__main__":
    main()
