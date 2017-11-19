{
    "targets": [
        {
            "target_name": "cryptonote",
            "sources": [
                "src/main.cc",
                "src/cryptonote_core/cryptonote_format_utils.cpp",
                "src/cryptonote_core/cryptonote_basic_impl.cpp",
                "src/crypto/tree-hash.c",
                "src/crypto/crypto.cpp",
                "src/crypto/crypto-ops.c",
                "src/crypto/crypto-ops-data.c",
                "src/crypto/hash.c",
                "src/crypto/keccak.c",
                "src/common/base58.cpp",
				
                "src/crypto/slow-hash.c",
                "src/cryptonote_core/difficulty.cpp",
                "src/cryptonote_core/miner.cpp",
                "src/crypto/crypto.cpp",
                "src/crypto/random.c",
                "src/crypto/hash-extra-blake.c",
                "src/crypto/hash-extra-groestl.c",
                "src/crypto/hash-extra-jh.c",
                "src/crypto/hash-extra-skein.c",
                "src/crypto/oaes_lib.c",
                "src/crypto/blake256.c",
                "src/crypto/groestl.c",
                "src/crypto/jh.c",
                "src/crypto/skein.c"
            ],
            "include_dirs": [
                "src",
                "src/contrib/epee/include",
				"<!(node -e \"require('nan')\")",
            ],
            "link_settings": {
                "libraries": [
                    "-lboost_system",
                    "-lboost_date_time",
					"-lboost_thread",
					"-lboost_filesystem",
					"-lboost_regex",
					"-lboost_program_options",
                ]
            },
            "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ],
            "cflags_cc": [
                  "-std=c++0x",
                  "-fexceptions",
                  "-frtti",
            ],
        }
    ]
}
