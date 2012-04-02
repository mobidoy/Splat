#
# Copyright (c) 2008-10, Mahadevan R All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  * Neither the name of this software, nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""Intrinsic IDs.

Intended to be imported into the llvm.core namespace. Not for public use."""


INTR_ALPHA_UMULH               = 1
INTR_ANNOTATION                = 2
INTR_ARM_NEON_VABALS           = 3
INTR_ARM_NEON_VABALU           = 4
INTR_ARM_NEON_VABAS            = 5
INTR_ARM_NEON_VABAU            = 6
INTR_ARM_NEON_VABDLS           = 7
INTR_ARM_NEON_VABDLU           = 8
INTR_ARM_NEON_VABDS            = 9
INTR_ARM_NEON_VABDU            = 10
INTR_ARM_NEON_VABS             = 11
INTR_ARM_NEON_VACGED           = 12
INTR_ARM_NEON_VACGEQ           = 13
INTR_ARM_NEON_VACGTD           = 14
INTR_ARM_NEON_VACGTQ           = 15
INTR_ARM_NEON_VADDHN           = 16
INTR_ARM_NEON_VADDLS           = 17
INTR_ARM_NEON_VADDLU           = 18
INTR_ARM_NEON_VADDWS           = 19
INTR_ARM_NEON_VADDWU           = 20
INTR_ARM_NEON_VCLS             = 21
INTR_ARM_NEON_VCLZ             = 22
INTR_ARM_NEON_VCNT             = 23
INTR_ARM_NEON_VCVTFP2FXS       = 24
INTR_ARM_NEON_VCVTFP2FXU       = 25
INTR_ARM_NEON_VCVTFXS2FP       = 26
INTR_ARM_NEON_VCVTFXU2FP       = 27
INTR_ARM_NEON_VHADDS           = 28
INTR_ARM_NEON_VHADDU           = 29
INTR_ARM_NEON_VHSUBS           = 30
INTR_ARM_NEON_VHSUBU           = 31
INTR_ARM_NEON_VLD1             = 32
INTR_ARM_NEON_VLD2             = 33
INTR_ARM_NEON_VLD2LANE         = 34
INTR_ARM_NEON_VLD3             = 35
INTR_ARM_NEON_VLD3LANE         = 36
INTR_ARM_NEON_VLD4             = 37
INTR_ARM_NEON_VLD4LANE         = 38
INTR_ARM_NEON_VMAXS            = 39
INTR_ARM_NEON_VMAXU            = 40
INTR_ARM_NEON_VMINS            = 41
INTR_ARM_NEON_VMINU            = 42
INTR_ARM_NEON_VMLALS           = 43
INTR_ARM_NEON_VMLALU           = 44
INTR_ARM_NEON_VMLSLS           = 45
INTR_ARM_NEON_VMLSLU           = 46
INTR_ARM_NEON_VMOVLS           = 47
INTR_ARM_NEON_VMOVLU           = 48
INTR_ARM_NEON_VMOVN            = 49
INTR_ARM_NEON_VMULLP           = 50
INTR_ARM_NEON_VMULLS           = 51
INTR_ARM_NEON_VMULLU           = 52
INTR_ARM_NEON_VMULP            = 53
INTR_ARM_NEON_VPADALS          = 54
INTR_ARM_NEON_VPADALU          = 55
INTR_ARM_NEON_VPADD            = 56
INTR_ARM_NEON_VPADDLS          = 57
INTR_ARM_NEON_VPADDLU          = 58
INTR_ARM_NEON_VPMAXS           = 59
INTR_ARM_NEON_VPMAXU           = 60
INTR_ARM_NEON_VPMINS           = 61
INTR_ARM_NEON_VPMINU           = 62
INTR_ARM_NEON_VQABS            = 63
INTR_ARM_NEON_VQADDS           = 64
INTR_ARM_NEON_VQADDU           = 65
INTR_ARM_NEON_VQDMLAL          = 66
INTR_ARM_NEON_VQDMLSL          = 67
INTR_ARM_NEON_VQDMULH          = 68
INTR_ARM_NEON_VQDMULL          = 69
INTR_ARM_NEON_VQMOVNS          = 70
INTR_ARM_NEON_VQMOVNSU         = 71
INTR_ARM_NEON_VQMOVNU          = 72
INTR_ARM_NEON_VQNEG            = 73
INTR_ARM_NEON_VQRDMULH         = 74
INTR_ARM_NEON_VQRSHIFTNS       = 75
INTR_ARM_NEON_VQRSHIFTNSU      = 76
INTR_ARM_NEON_VQRSHIFTNU       = 77
INTR_ARM_NEON_VQRSHIFTS        = 78
INTR_ARM_NEON_VQRSHIFTU        = 79
INTR_ARM_NEON_VQSHIFTNS        = 80
INTR_ARM_NEON_VQSHIFTNSU       = 81
INTR_ARM_NEON_VQSHIFTNU        = 82
INTR_ARM_NEON_VQSHIFTS         = 83
INTR_ARM_NEON_VQSHIFTSU        = 84
INTR_ARM_NEON_VQSHIFTU         = 85
INTR_ARM_NEON_VQSUBS           = 86
INTR_ARM_NEON_VQSUBU           = 87
INTR_ARM_NEON_VRADDHN          = 88
INTR_ARM_NEON_VRECPE           = 89
INTR_ARM_NEON_VRECPS           = 90
INTR_ARM_NEON_VRHADDS          = 91
INTR_ARM_NEON_VRHADDU          = 92
INTR_ARM_NEON_VRSHIFTN         = 93
INTR_ARM_NEON_VRSHIFTS         = 94
INTR_ARM_NEON_VRSHIFTU         = 95
INTR_ARM_NEON_VRSQRTE          = 96
INTR_ARM_NEON_VRSQRTS          = 97
INTR_ARM_NEON_VRSUBHN          = 98
INTR_ARM_NEON_VSHIFTINS        = 99
INTR_ARM_NEON_VSHIFTLS         = 100
INTR_ARM_NEON_VSHIFTLU         = 101
INTR_ARM_NEON_VSHIFTN          = 102
INTR_ARM_NEON_VSHIFTS          = 103
INTR_ARM_NEON_VSHIFTU          = 104
INTR_ARM_NEON_VST1             = 105
INTR_ARM_NEON_VST2             = 106
INTR_ARM_NEON_VST2LANE         = 107
INTR_ARM_NEON_VST3             = 108
INTR_ARM_NEON_VST3LANE         = 109
INTR_ARM_NEON_VST4             = 110
INTR_ARM_NEON_VST4LANE         = 111
INTR_ARM_NEON_VSUBHN           = 112
INTR_ARM_NEON_VSUBLS           = 113
INTR_ARM_NEON_VSUBLU           = 114
INTR_ARM_NEON_VSUBWS           = 115
INTR_ARM_NEON_VSUBWU           = 116
INTR_ARM_NEON_VTBL1            = 117
INTR_ARM_NEON_VTBL2            = 118
INTR_ARM_NEON_VTBL3            = 119
INTR_ARM_NEON_VTBL4            = 120
INTR_ARM_NEON_VTBX1            = 121
INTR_ARM_NEON_VTBX2            = 122
INTR_ARM_NEON_VTBX3            = 123
INTR_ARM_NEON_VTBX4            = 124
INTR_ARM_THREAD_POINTER        = 125
INTR_ATOMIC_CMP_SWAP           = 126
INTR_ATOMIC_LOAD_ADD           = 127
INTR_ATOMIC_LOAD_AND           = 128
INTR_ATOMIC_LOAD_MAX           = 129
INTR_ATOMIC_LOAD_MIN           = 130
INTR_ATOMIC_LOAD_NAND          = 131
INTR_ATOMIC_LOAD_OR            = 132
INTR_ATOMIC_LOAD_SUB           = 133
INTR_ATOMIC_LOAD_UMAX          = 134
INTR_ATOMIC_LOAD_UMIN          = 135
INTR_ATOMIC_LOAD_XOR           = 136
INTR_ATOMIC_SWAP               = 137
INTR_BSWAP                     = 138
INTR_CONVERTFF                 = 139
INTR_CONVERTFSI                = 140
INTR_CONVERTFUI                = 141
INTR_CONVERTSIF                = 142
INTR_CONVERTSS                 = 143
INTR_CONVERTSU                 = 144
INTR_CONVERTUIF                = 145
INTR_CONVERTUS                 = 146
INTR_CONVERTUU                 = 147
INTR_COS                       = 148
INTR_CTLZ                      = 149
INTR_CTPOP                     = 150
INTR_CTTZ                      = 151
INTR_DBG_DECLARE               = 152
INTR_DBG_VALUE                 = 153
INTR_EH_DWARF_CFA              = 154
INTR_EH_EXCEPTION              = 155
INTR_EH_RETURN_I32             = 156
INTR_EH_RETURN_I64             = 157
INTR_EH_SELECTOR               = 158
INTR_EH_SJLJ_CALLSITE          = 159
INTR_EH_SJLJ_LONGJMP           = 160
INTR_EH_SJLJ_LSDA              = 161
INTR_EH_SJLJ_SETJMP            = 162
INTR_EH_TYPEID_FOR             = 163
INTR_EH_UNWIND_INIT            = 164
INTR_EXP                       = 165
INTR_EXP2                      = 166
INTR_FLT_ROUNDS                = 167
INTR_FRAMEADDRESS              = 168
INTR_GCREAD                    = 169
INTR_GCROOT                    = 170
INTR_GCWRITE                   = 171
INTR_INIT_TRAMPOLINE           = 172
INTR_INVARIANT_END             = 173
INTR_INVARIANT_START           = 174
INTR_LIFETIME_END              = 175
INTR_LIFETIME_START            = 176
INTR_LOG                       = 177
INTR_LOG10                     = 178
INTR_LOG2                      = 179
INTR_LONGJMP                   = 180
INTR_MEMCPY                    = 181
INTR_MEMMOVE                   = 182
INTR_MEMORY_BARRIER            = 183
INTR_MEMSET                    = 184
INTR_OBJECTSIZE                = 185
INTR_PCMARKER                  = 186
INTR_POW                       = 187
INTR_POWI                      = 188
INTR_PPC_ALTIVEC_DSS           = 189
INTR_PPC_ALTIVEC_DSSALL        = 190
INTR_PPC_ALTIVEC_DST           = 191
INTR_PPC_ALTIVEC_DSTST         = 192
INTR_PPC_ALTIVEC_DSTSTT        = 193
INTR_PPC_ALTIVEC_DSTT          = 194
INTR_PPC_ALTIVEC_LVEBX         = 195
INTR_PPC_ALTIVEC_LVEHX         = 196
INTR_PPC_ALTIVEC_LVEWX         = 197
INTR_PPC_ALTIVEC_LVSL          = 198
INTR_PPC_ALTIVEC_LVSR          = 199
INTR_PPC_ALTIVEC_LVX           = 200
INTR_PPC_ALTIVEC_LVXL          = 201
INTR_PPC_ALTIVEC_MFVSCR        = 202
INTR_PPC_ALTIVEC_MTVSCR        = 203
INTR_PPC_ALTIVEC_STVEBX        = 204
INTR_PPC_ALTIVEC_STVEHX        = 205
INTR_PPC_ALTIVEC_STVEWX        = 206
INTR_PPC_ALTIVEC_STVX          = 207
INTR_PPC_ALTIVEC_STVXL         = 208
INTR_PPC_ALTIVEC_VADDCUW       = 209
INTR_PPC_ALTIVEC_VADDSBS       = 210
INTR_PPC_ALTIVEC_VADDSHS       = 211
INTR_PPC_ALTIVEC_VADDSWS       = 212
INTR_PPC_ALTIVEC_VADDUBS       = 213
INTR_PPC_ALTIVEC_VADDUHS       = 214
INTR_PPC_ALTIVEC_VADDUWS       = 215
INTR_PPC_ALTIVEC_VAVGSB        = 216
INTR_PPC_ALTIVEC_VAVGSH        = 217
INTR_PPC_ALTIVEC_VAVGSW        = 218
INTR_PPC_ALTIVEC_VAVGUB        = 219
INTR_PPC_ALTIVEC_VAVGUH        = 220
INTR_PPC_ALTIVEC_VAVGUW        = 221
INTR_PPC_ALTIVEC_VCFSX         = 222
INTR_PPC_ALTIVEC_VCFUX         = 223
INTR_PPC_ALTIVEC_VCMPBFP       = 224
INTR_PPC_ALTIVEC_VCMPBFP_P     = 225
INTR_PPC_ALTIVEC_VCMPEQFP      = 226
INTR_PPC_ALTIVEC_VCMPEQFP_P    = 227
INTR_PPC_ALTIVEC_VCMPEQUB      = 228
INTR_PPC_ALTIVEC_VCMPEQUB_P    = 229
INTR_PPC_ALTIVEC_VCMPEQUH      = 230
INTR_PPC_ALTIVEC_VCMPEQUH_P    = 231
INTR_PPC_ALTIVEC_VCMPEQUW      = 232
INTR_PPC_ALTIVEC_VCMPEQUW_P    = 233
INTR_PPC_ALTIVEC_VCMPGEFP      = 234
INTR_PPC_ALTIVEC_VCMPGEFP_P    = 235
INTR_PPC_ALTIVEC_VCMPGTFP      = 236
INTR_PPC_ALTIVEC_VCMPGTFP_P    = 237
INTR_PPC_ALTIVEC_VCMPGTSB      = 238
INTR_PPC_ALTIVEC_VCMPGTSB_P    = 239
INTR_PPC_ALTIVEC_VCMPGTSH      = 240
INTR_PPC_ALTIVEC_VCMPGTSH_P    = 241
INTR_PPC_ALTIVEC_VCMPGTSW      = 242
INTR_PPC_ALTIVEC_VCMPGTSW_P    = 243
INTR_PPC_ALTIVEC_VCMPGTUB      = 244
INTR_PPC_ALTIVEC_VCMPGTUB_P    = 245
INTR_PPC_ALTIVEC_VCMPGTUH      = 246
INTR_PPC_ALTIVEC_VCMPGTUH_P    = 247
INTR_PPC_ALTIVEC_VCMPGTUW      = 248
INTR_PPC_ALTIVEC_VCMPGTUW_P    = 249
INTR_PPC_ALTIVEC_VCTSXS        = 250
INTR_PPC_ALTIVEC_VCTUXS        = 251
INTR_PPC_ALTIVEC_VEXPTEFP      = 252
INTR_PPC_ALTIVEC_VLOGEFP       = 253
INTR_PPC_ALTIVEC_VMADDFP       = 254
INTR_PPC_ALTIVEC_VMAXFP        = 255
INTR_PPC_ALTIVEC_VMAXSB        = 256
INTR_PPC_ALTIVEC_VMAXSH        = 257
INTR_PPC_ALTIVEC_VMAXSW        = 258
INTR_PPC_ALTIVEC_VMAXUB        = 259
INTR_PPC_ALTIVEC_VMAXUH        = 260
INTR_PPC_ALTIVEC_VMAXUW        = 261
INTR_PPC_ALTIVEC_VMHADDSHS     = 262
INTR_PPC_ALTIVEC_VMHRADDSHS    = 263
INTR_PPC_ALTIVEC_VMINFP        = 264
INTR_PPC_ALTIVEC_VMINSB        = 265
INTR_PPC_ALTIVEC_VMINSH        = 266
INTR_PPC_ALTIVEC_VMINSW        = 267
INTR_PPC_ALTIVEC_VMINUB        = 268
INTR_PPC_ALTIVEC_VMINUH        = 269
INTR_PPC_ALTIVEC_VMINUW        = 270
INTR_PPC_ALTIVEC_VMLADDUHM     = 271
INTR_PPC_ALTIVEC_VMSUMMBM      = 272
INTR_PPC_ALTIVEC_VMSUMSHM      = 273
INTR_PPC_ALTIVEC_VMSUMSHS      = 274
INTR_PPC_ALTIVEC_VMSUMUBM      = 275
INTR_PPC_ALTIVEC_VMSUMUHM      = 276
INTR_PPC_ALTIVEC_VMSUMUHS      = 277
INTR_PPC_ALTIVEC_VMULESB       = 278
INTR_PPC_ALTIVEC_VMULESH       = 279
INTR_PPC_ALTIVEC_VMULEUB       = 280
INTR_PPC_ALTIVEC_VMULEUH       = 281
INTR_PPC_ALTIVEC_VMULOSB       = 282
INTR_PPC_ALTIVEC_VMULOSH       = 283
INTR_PPC_ALTIVEC_VMULOUB       = 284
INTR_PPC_ALTIVEC_VMULOUH       = 285
INTR_PPC_ALTIVEC_VNMSUBFP      = 286
INTR_PPC_ALTIVEC_VPERM         = 287
INTR_PPC_ALTIVEC_VPKPX         = 288
INTR_PPC_ALTIVEC_VPKSHSS       = 289
INTR_PPC_ALTIVEC_VPKSHUS       = 290
INTR_PPC_ALTIVEC_VPKSWSS       = 291
INTR_PPC_ALTIVEC_VPKSWUS       = 292
INTR_PPC_ALTIVEC_VPKUHUS       = 293
INTR_PPC_ALTIVEC_VPKUWUS       = 294
INTR_PPC_ALTIVEC_VREFP         = 295
INTR_PPC_ALTIVEC_VRFIM         = 296
INTR_PPC_ALTIVEC_VRFIN         = 297
INTR_PPC_ALTIVEC_VRFIP         = 298
INTR_PPC_ALTIVEC_VRFIZ         = 299
INTR_PPC_ALTIVEC_VRLB          = 300
INTR_PPC_ALTIVEC_VRLH          = 301
INTR_PPC_ALTIVEC_VRLW          = 302
INTR_PPC_ALTIVEC_VRSQRTEFP     = 303
INTR_PPC_ALTIVEC_VSEL          = 304
INTR_PPC_ALTIVEC_VSL           = 305
INTR_PPC_ALTIVEC_VSLB          = 306
INTR_PPC_ALTIVEC_VSLH          = 307
INTR_PPC_ALTIVEC_VSLO          = 308
INTR_PPC_ALTIVEC_VSLW          = 309
INTR_PPC_ALTIVEC_VSR           = 310
INTR_PPC_ALTIVEC_VSRAB         = 311
INTR_PPC_ALTIVEC_VSRAH         = 312
INTR_PPC_ALTIVEC_VSRAW         = 313
INTR_PPC_ALTIVEC_VSRB          = 314
INTR_PPC_ALTIVEC_VSRH          = 315
INTR_PPC_ALTIVEC_VSRO          = 316
INTR_PPC_ALTIVEC_VSRW          = 317
INTR_PPC_ALTIVEC_VSUBCUW       = 318
INTR_PPC_ALTIVEC_VSUBSBS       = 319
INTR_PPC_ALTIVEC_VSUBSHS       = 320
INTR_PPC_ALTIVEC_VSUBSWS       = 321
INTR_PPC_ALTIVEC_VSUBUBS       = 322
INTR_PPC_ALTIVEC_VSUBUHS       = 323
INTR_PPC_ALTIVEC_VSUBUWS       = 324
INTR_PPC_ALTIVEC_VSUM2SWS      = 325
INTR_PPC_ALTIVEC_VSUM4SBS      = 326
INTR_PPC_ALTIVEC_VSUM4SHS      = 327
INTR_PPC_ALTIVEC_VSUM4UBS      = 328
INTR_PPC_ALTIVEC_VSUMSWS       = 329
INTR_PPC_ALTIVEC_VUPKHPX       = 330
INTR_PPC_ALTIVEC_VUPKHSB       = 331
INTR_PPC_ALTIVEC_VUPKHSH       = 332
INTR_PPC_ALTIVEC_VUPKLPX       = 333
INTR_PPC_ALTIVEC_VUPKLSB       = 334
INTR_PPC_ALTIVEC_VUPKLSH       = 335
INTR_PPC_DCBA                  = 336
INTR_PPC_DCBF                  = 337
INTR_PPC_DCBI                  = 338
INTR_PPC_DCBST                 = 339
INTR_PPC_DCBT                  = 340
INTR_PPC_DCBTST                = 341
INTR_PPC_DCBZ                  = 342
INTR_PPC_DCBZL                 = 343
INTR_PPC_SYNC                  = 344
INTR_PREFETCH                  = 345
INTR_PTR_ANNOTATION            = 346
INTR_READCYCLECOUNTER          = 347
INTR_RETURNADDRESS             = 348
INTR_SADD_WITH_OVERFLOW        = 349
INTR_SETJMP                    = 350
INTR_SIGLONGJMP                = 351
INTR_SIGSETJMP                 = 352
INTR_SIN                       = 353
INTR_SMUL_WITH_OVERFLOW        = 354
INTR_SPU_SI_A                  = 355
INTR_SPU_SI_ADDX               = 356
INTR_SPU_SI_AH                 = 357
INTR_SPU_SI_AHI                = 358
INTR_SPU_SI_AI                 = 359
INTR_SPU_SI_AND                = 360
INTR_SPU_SI_ANDBI              = 361
INTR_SPU_SI_ANDC               = 362
INTR_SPU_SI_ANDHI              = 363
INTR_SPU_SI_ANDI               = 364
INTR_SPU_SI_BG                 = 365
INTR_SPU_SI_BGX                = 366
INTR_SPU_SI_CEQ                = 367
INTR_SPU_SI_CEQB               = 368
INTR_SPU_SI_CEQBI              = 369
INTR_SPU_SI_CEQH               = 370
INTR_SPU_SI_CEQHI              = 371
INTR_SPU_SI_CEQI               = 372
INTR_SPU_SI_CG                 = 373
INTR_SPU_SI_CGT                = 374
INTR_SPU_SI_CGTB               = 375
INTR_SPU_SI_CGTBI              = 376
INTR_SPU_SI_CGTH               = 377
INTR_SPU_SI_CGTHI              = 378
INTR_SPU_SI_CGTI               = 379
INTR_SPU_SI_CGX                = 380
INTR_SPU_SI_CLGT               = 381
INTR_SPU_SI_CLGTB              = 382
INTR_SPU_SI_CLGTBI             = 383
INTR_SPU_SI_CLGTH              = 384
INTR_SPU_SI_CLGTHI             = 385
INTR_SPU_SI_CLGTI              = 386
INTR_SPU_SI_DFA                = 387
INTR_SPU_SI_DFM                = 388
INTR_SPU_SI_DFMA               = 389
INTR_SPU_SI_DFMS               = 390
INTR_SPU_SI_DFNMA              = 391
INTR_SPU_SI_DFNMS              = 392
INTR_SPU_SI_DFS                = 393
INTR_SPU_SI_FA                 = 394
INTR_SPU_SI_FCEQ               = 395
INTR_SPU_SI_FCGT               = 396
INTR_SPU_SI_FCMEQ              = 397
INTR_SPU_SI_FCMGT              = 398
INTR_SPU_SI_FM                 = 399
INTR_SPU_SI_FMA                = 400
INTR_SPU_SI_FMS                = 401
INTR_SPU_SI_FNMS               = 402
INTR_SPU_SI_FS                 = 403
INTR_SPU_SI_FSMBI              = 404
INTR_SPU_SI_MPY                = 405
INTR_SPU_SI_MPYA               = 406
INTR_SPU_SI_MPYH               = 407
INTR_SPU_SI_MPYHH              = 408
INTR_SPU_SI_MPYHHA             = 409
INTR_SPU_SI_MPYHHAU            = 410
INTR_SPU_SI_MPYHHU             = 411
INTR_SPU_SI_MPYI               = 412
INTR_SPU_SI_MPYS               = 413
INTR_SPU_SI_MPYU               = 414
INTR_SPU_SI_MPYUI              = 415
INTR_SPU_SI_NAND               = 416
INTR_SPU_SI_NOR                = 417
INTR_SPU_SI_OR                 = 418
INTR_SPU_SI_ORBI               = 419
INTR_SPU_SI_ORC                = 420
INTR_SPU_SI_ORHI               = 421
INTR_SPU_SI_ORI                = 422
INTR_SPU_SI_SF                 = 423
INTR_SPU_SI_SFH                = 424
INTR_SPU_SI_SFHI               = 425
INTR_SPU_SI_SFI                = 426
INTR_SPU_SI_SFX                = 427
INTR_SPU_SI_SHLI               = 428
INTR_SPU_SI_SHLQBI             = 429
INTR_SPU_SI_SHLQBII            = 430
INTR_SPU_SI_SHLQBY             = 431
INTR_SPU_SI_SHLQBYI            = 432
INTR_SPU_SI_XOR                = 433
INTR_SPU_SI_XORBI              = 434
INTR_SPU_SI_XORHI              = 435
INTR_SPU_SI_XORI               = 436
INTR_SQRT                      = 437
INTR_SSUB_WITH_OVERFLOW        = 438
INTR_STACKPROTECTOR            = 439
INTR_STACKRESTORE              = 440
INTR_STACKSAVE                 = 441
INTR_TRAP                      = 442
INTR_UADD_WITH_OVERFLOW        = 443
INTR_UMUL_WITH_OVERFLOW        = 444
INTR_USUB_WITH_OVERFLOW        = 445
INTR_VACOPY                    = 446
INTR_VAEND                     = 447
INTR_VAR_ANNOTATION            = 448
INTR_VASTART                   = 449
INTR_X86_MMX_EMMS              = 450
INTR_X86_MMX_FEMMS             = 451
INTR_X86_MMX_MASKMOVQ          = 452
INTR_X86_MMX_MOVNT_DQ          = 453
INTR_X86_MMX_PACKSSDW          = 454
INTR_X86_MMX_PACKSSWB          = 455
INTR_X86_MMX_PACKUSWB          = 456
INTR_X86_MMX_PADDS_B           = 457
INTR_X86_MMX_PADDS_W           = 458
INTR_X86_MMX_PADDUS_B          = 459
INTR_X86_MMX_PADDUS_W          = 460
INTR_X86_MMX_PAVG_B            = 461
INTR_X86_MMX_PAVG_W            = 462
INTR_X86_MMX_PCMPEQ_B          = 463
INTR_X86_MMX_PCMPEQ_D          = 464
INTR_X86_MMX_PCMPEQ_W          = 465
INTR_X86_MMX_PCMPGT_B          = 466
INTR_X86_MMX_PCMPGT_D          = 467
INTR_X86_MMX_PCMPGT_W          = 468
INTR_X86_MMX_PMADD_WD          = 469
INTR_X86_MMX_PMAXS_W           = 470
INTR_X86_MMX_PMAXU_B           = 471
INTR_X86_MMX_PMINS_W           = 472
INTR_X86_MMX_PMINU_B           = 473
INTR_X86_MMX_PMOVMSKB          = 474
INTR_X86_MMX_PMULH_W           = 475
INTR_X86_MMX_PMULHU_W          = 476
INTR_X86_MMX_PMULU_DQ          = 477
INTR_X86_MMX_PSAD_BW           = 478
INTR_X86_MMX_PSLL_D            = 479
INTR_X86_MMX_PSLL_Q            = 480
INTR_X86_MMX_PSLL_W            = 481
INTR_X86_MMX_PSLLI_D           = 482
INTR_X86_MMX_PSLLI_Q           = 483
INTR_X86_MMX_PSLLI_W           = 484
INTR_X86_MMX_PSRA_D            = 485
INTR_X86_MMX_PSRA_W            = 486
INTR_X86_MMX_PSRAI_D           = 487
INTR_X86_MMX_PSRAI_W           = 488
INTR_X86_MMX_PSRL_D            = 489
INTR_X86_MMX_PSRL_Q            = 490
INTR_X86_MMX_PSRL_W            = 491
INTR_X86_MMX_PSRLI_D           = 492
INTR_X86_MMX_PSRLI_Q           = 493
INTR_X86_MMX_PSRLI_W           = 494
INTR_X86_MMX_PSUBS_B           = 495
INTR_X86_MMX_PSUBS_W           = 496
INTR_X86_MMX_PSUBUS_B          = 497
INTR_X86_MMX_PSUBUS_W          = 498
INTR_X86_SSE2_ADD_SD           = 499
INTR_X86_SSE2_CLFLUSH          = 500
INTR_X86_SSE2_CMP_PD           = 501
INTR_X86_SSE2_CMP_SD           = 502
INTR_X86_SSE2_COMIEQ_SD        = 503
INTR_X86_SSE2_COMIGE_SD        = 504
INTR_X86_SSE2_COMIGT_SD        = 505
INTR_X86_SSE2_COMILE_SD        = 506
INTR_X86_SSE2_COMILT_SD        = 507
INTR_X86_SSE2_COMINEQ_SD       = 508
INTR_X86_SSE2_CVTDQ2PD         = 509
INTR_X86_SSE2_CVTDQ2PS         = 510
INTR_X86_SSE2_CVTPD2DQ         = 511
INTR_X86_SSE2_CVTPD2PS         = 512
INTR_X86_SSE2_CVTPS2DQ         = 513
INTR_X86_SSE2_CVTPS2PD         = 514
INTR_X86_SSE2_CVTSD2SI         = 515
INTR_X86_SSE2_CVTSD2SI64       = 516
INTR_X86_SSE2_CVTSD2SS         = 517
INTR_X86_SSE2_CVTSI2SD         = 518
INTR_X86_SSE2_CVTSI642SD       = 519
INTR_X86_SSE2_CVTSS2SD         = 520
INTR_X86_SSE2_CVTTPD2DQ        = 521
INTR_X86_SSE2_CVTTPS2DQ        = 522
INTR_X86_SSE2_CVTTSD2SI        = 523
INTR_X86_SSE2_CVTTSD2SI64      = 524
INTR_X86_SSE2_DIV_SD           = 525
INTR_X86_SSE2_LFENCE           = 526
INTR_X86_SSE2_LOADU_DQ         = 527
INTR_X86_SSE2_LOADU_PD         = 528
INTR_X86_SSE2_MASKMOV_DQU      = 529
INTR_X86_SSE2_MAX_PD           = 530
INTR_X86_SSE2_MAX_SD           = 531
INTR_X86_SSE2_MFENCE           = 532
INTR_X86_SSE2_MIN_PD           = 533
INTR_X86_SSE2_MIN_SD           = 534
INTR_X86_SSE2_MOVMSK_PD        = 535
INTR_X86_SSE2_MOVNT_DQ         = 536
INTR_X86_SSE2_MOVNT_I          = 537
INTR_X86_SSE2_MOVNT_PD         = 538
INTR_X86_SSE2_MUL_SD           = 539
INTR_X86_SSE2_PACKSSDW_128     = 540
INTR_X86_SSE2_PACKSSWB_128     = 541
INTR_X86_SSE2_PACKUSWB_128     = 542
INTR_X86_SSE2_PADDS_B          = 543
INTR_X86_SSE2_PADDS_W          = 544
INTR_X86_SSE2_PADDUS_B         = 545
INTR_X86_SSE2_PADDUS_W         = 546
INTR_X86_SSE2_PAVG_B           = 547
INTR_X86_SSE2_PAVG_W           = 548
INTR_X86_SSE2_PCMPEQ_B         = 549
INTR_X86_SSE2_PCMPEQ_D         = 550
INTR_X86_SSE2_PCMPEQ_W         = 551
INTR_X86_SSE2_PCMPGT_B         = 552
INTR_X86_SSE2_PCMPGT_D         = 553
INTR_X86_SSE2_PCMPGT_W         = 554
INTR_X86_SSE2_PMADD_WD         = 555
INTR_X86_SSE2_PMAXS_W          = 556
INTR_X86_SSE2_PMAXU_B          = 557
INTR_X86_SSE2_PMINS_W          = 558
INTR_X86_SSE2_PMINU_B          = 559
INTR_X86_SSE2_PMOVMSKB_128     = 560
INTR_X86_SSE2_PMULH_W          = 561
INTR_X86_SSE2_PMULHU_W         = 562
INTR_X86_SSE2_PMULU_DQ         = 563
INTR_X86_SSE2_PSAD_BW          = 564
INTR_X86_SSE2_PSLL_D           = 565
INTR_X86_SSE2_PSLL_DQ          = 566
INTR_X86_SSE2_PSLL_DQ_BS       = 567
INTR_X86_SSE2_PSLL_Q           = 568
INTR_X86_SSE2_PSLL_W           = 569
INTR_X86_SSE2_PSLLI_D          = 570
INTR_X86_SSE2_PSLLI_Q          = 571
INTR_X86_SSE2_PSLLI_W          = 572
INTR_X86_SSE2_PSRA_D           = 573
INTR_X86_SSE2_PSRA_W           = 574
INTR_X86_SSE2_PSRAI_D          = 575
INTR_X86_SSE2_PSRAI_W          = 576
INTR_X86_SSE2_PSRL_D           = 577
INTR_X86_SSE2_PSRL_DQ          = 578
INTR_X86_SSE2_PSRL_DQ_BS       = 579
INTR_X86_SSE2_PSRL_Q           = 580
INTR_X86_SSE2_PSRL_W           = 581
INTR_X86_SSE2_PSRLI_D          = 582
INTR_X86_SSE2_PSRLI_Q          = 583
INTR_X86_SSE2_PSRLI_W          = 584
INTR_X86_SSE2_PSUBS_B          = 585
INTR_X86_SSE2_PSUBS_W          = 586
INTR_X86_SSE2_PSUBUS_B         = 587
INTR_X86_SSE2_PSUBUS_W         = 588
INTR_X86_SSE2_SQRT_PD          = 589
INTR_X86_SSE2_SQRT_SD          = 590
INTR_X86_SSE2_STOREL_DQ        = 591
INTR_X86_SSE2_STOREU_DQ        = 592
INTR_X86_SSE2_STOREU_PD        = 593
INTR_X86_SSE2_SUB_SD           = 594
INTR_X86_SSE2_UCOMIEQ_SD       = 595
INTR_X86_SSE2_UCOMIGE_SD       = 596
INTR_X86_SSE2_UCOMIGT_SD       = 597
INTR_X86_SSE2_UCOMILE_SD       = 598
INTR_X86_SSE2_UCOMILT_SD       = 599
INTR_X86_SSE2_UCOMINEQ_SD      = 600
INTR_X86_SSE3_ADDSUB_PD        = 601
INTR_X86_SSE3_ADDSUB_PS        = 602
INTR_X86_SSE3_HADD_PD          = 603
INTR_X86_SSE3_HADD_PS          = 604
INTR_X86_SSE3_HSUB_PD          = 605
INTR_X86_SSE3_HSUB_PS          = 606
INTR_X86_SSE3_LDU_DQ           = 607
INTR_X86_SSE3_MONITOR          = 608
INTR_X86_SSE3_MWAIT            = 609
INTR_X86_SSE41_BLENDPD         = 610
INTR_X86_SSE41_BLENDPS         = 611
INTR_X86_SSE41_BLENDVPD        = 612
INTR_X86_SSE41_BLENDVPS        = 613
INTR_X86_SSE41_DPPD            = 614
INTR_X86_SSE41_DPPS            = 615
INTR_X86_SSE41_EXTRACTPS       = 616
INTR_X86_SSE41_INSERTPS        = 617
INTR_X86_SSE41_MOVNTDQA        = 618
INTR_X86_SSE41_MPSADBW         = 619
INTR_X86_SSE41_PACKUSDW        = 620
INTR_X86_SSE41_PBLENDVB        = 621
INTR_X86_SSE41_PBLENDW         = 622
INTR_X86_SSE41_PCMPEQQ         = 623
INTR_X86_SSE41_PEXTRB          = 624
INTR_X86_SSE41_PEXTRD          = 625
INTR_X86_SSE41_PEXTRQ          = 626
INTR_X86_SSE41_PHMINPOSUW      = 627
INTR_X86_SSE41_PMAXSB          = 628
INTR_X86_SSE41_PMAXSD          = 629
INTR_X86_SSE41_PMAXUD          = 630
INTR_X86_SSE41_PMAXUW          = 631
INTR_X86_SSE41_PMINSB          = 632
INTR_X86_SSE41_PMINSD          = 633
INTR_X86_SSE41_PMINUD          = 634
INTR_X86_SSE41_PMINUW          = 635
INTR_X86_SSE41_PMOVSXBD        = 636
INTR_X86_SSE41_PMOVSXBQ        = 637
INTR_X86_SSE41_PMOVSXBW        = 638
INTR_X86_SSE41_PMOVSXDQ        = 639
INTR_X86_SSE41_PMOVSXWD        = 640
INTR_X86_SSE41_PMOVSXWQ        = 641
INTR_X86_SSE41_PMOVZXBD        = 642
INTR_X86_SSE41_PMOVZXBQ        = 643
INTR_X86_SSE41_PMOVZXBW        = 644
INTR_X86_SSE41_PMOVZXDQ        = 645
INTR_X86_SSE41_PMOVZXWD        = 646
INTR_X86_SSE41_PMOVZXWQ        = 647
INTR_X86_SSE41_PMULDQ          = 648
INTR_X86_SSE41_PMULLD          = 649
INTR_X86_SSE41_PTESTC          = 650
INTR_X86_SSE41_PTESTNZC        = 651
INTR_X86_SSE41_PTESTZ          = 652
INTR_X86_SSE41_ROUND_PD        = 653
INTR_X86_SSE41_ROUND_PS        = 654
INTR_X86_SSE41_ROUND_SD        = 655
INTR_X86_SSE41_ROUND_SS        = 656
INTR_X86_SSE42_CRC32_16        = 657
INTR_X86_SSE42_CRC32_32        = 658
INTR_X86_SSE42_CRC32_64        = 659
INTR_X86_SSE42_CRC32_8         = 660
INTR_X86_SSE42_PCMPESTRI128    = 661
INTR_X86_SSE42_PCMPESTRIA128   = 662
INTR_X86_SSE42_PCMPESTRIC128   = 663
INTR_X86_SSE42_PCMPESTRIO128   = 664
INTR_X86_SSE42_PCMPESTRIS128   = 665
INTR_X86_SSE42_PCMPESTRIZ128   = 666
INTR_X86_SSE42_PCMPESTRM128    = 667
INTR_X86_SSE42_PCMPGTQ         = 668
INTR_X86_SSE42_PCMPISTRI128    = 669
INTR_X86_SSE42_PCMPISTRIA128   = 670
INTR_X86_SSE42_PCMPISTRIC128   = 671
INTR_X86_SSE42_PCMPISTRIO128   = 672
INTR_X86_SSE42_PCMPISTRIS128   = 673
INTR_X86_SSE42_PCMPISTRIZ128   = 674
INTR_X86_SSE42_PCMPISTRM128    = 675
INTR_X86_SSE_ADD_SS            = 676
INTR_X86_SSE_CMP_PS            = 677
INTR_X86_SSE_CMP_SS            = 678
INTR_X86_SSE_COMIEQ_SS         = 679
INTR_X86_SSE_COMIGE_SS         = 680
INTR_X86_SSE_COMIGT_SS         = 681
INTR_X86_SSE_COMILE_SS         = 682
INTR_X86_SSE_COMILT_SS         = 683
INTR_X86_SSE_COMINEQ_SS        = 684
INTR_X86_SSE_CVTPD2PI          = 685
INTR_X86_SSE_CVTPI2PD          = 686
INTR_X86_SSE_CVTPI2PS          = 687
INTR_X86_SSE_CVTPS2PI          = 688
INTR_X86_SSE_CVTSI2SS          = 689
INTR_X86_SSE_CVTSI642SS        = 690
INTR_X86_SSE_CVTSS2SI          = 691
INTR_X86_SSE_CVTSS2SI64        = 692
INTR_X86_SSE_CVTTPD2PI         = 693
INTR_X86_SSE_CVTTPS2PI         = 694
INTR_X86_SSE_CVTTSS2SI         = 695
INTR_X86_SSE_CVTTSS2SI64       = 696
INTR_X86_SSE_DIV_SS            = 697
INTR_X86_SSE_LDMXCSR           = 698
INTR_X86_SSE_LOADU_PS          = 699
INTR_X86_SSE_MAX_PS            = 700
INTR_X86_SSE_MAX_SS            = 701
INTR_X86_SSE_MIN_PS            = 702
INTR_X86_SSE_MIN_SS            = 703
INTR_X86_SSE_MOVMSK_PS         = 704
INTR_X86_SSE_MOVNT_PS          = 705
INTR_X86_SSE_MUL_SS            = 706
INTR_X86_SSE_RCP_PS            = 707
INTR_X86_SSE_RCP_SS            = 708
INTR_X86_SSE_RSQRT_PS          = 709
INTR_X86_SSE_RSQRT_SS          = 710
INTR_X86_SSE_SFENCE            = 711
INTR_X86_SSE_SQRT_PS           = 712
INTR_X86_SSE_SQRT_SS           = 713
INTR_X86_SSE_STMXCSR           = 714
INTR_X86_SSE_STOREU_PS         = 715
INTR_X86_SSE_SUB_SS            = 716
INTR_X86_SSE_UCOMIEQ_SS        = 717
INTR_X86_SSE_UCOMIGE_SS        = 718
INTR_X86_SSE_UCOMIGT_SS        = 719
INTR_X86_SSE_UCOMILE_SS        = 720
INTR_X86_SSE_UCOMILT_SS        = 721
INTR_X86_SSE_UCOMINEQ_SS       = 722
INTR_X86_SSSE3_PABS_B          = 723
INTR_X86_SSSE3_PABS_B_128      = 724
INTR_X86_SSSE3_PABS_D          = 725
INTR_X86_SSSE3_PABS_D_128      = 726
INTR_X86_SSSE3_PABS_W          = 727
INTR_X86_SSSE3_PABS_W_128      = 728
INTR_X86_SSSE3_PALIGN_R        = 729
INTR_X86_SSSE3_PALIGN_R_128    = 730
INTR_X86_SSSE3_PHADD_D         = 731
INTR_X86_SSSE3_PHADD_D_128     = 732
INTR_X86_SSSE3_PHADD_SW        = 733
INTR_X86_SSSE3_PHADD_SW_128    = 734
INTR_X86_SSSE3_PHADD_W         = 735
INTR_X86_SSSE3_PHADD_W_128     = 736
INTR_X86_SSSE3_PHSUB_D         = 737
INTR_X86_SSSE3_PHSUB_D_128     = 738
INTR_X86_SSSE3_PHSUB_SW        = 739
INTR_X86_SSSE3_PHSUB_SW_128    = 740
INTR_X86_SSSE3_PHSUB_W         = 741
INTR_X86_SSSE3_PHSUB_W_128     = 742
INTR_X86_SSSE3_PMADD_UB_SW     = 743
INTR_X86_SSSE3_PMADD_UB_SW_128 = 744
INTR_X86_SSSE3_PMUL_HR_SW      = 745
INTR_X86_SSSE3_PMUL_HR_SW_128  = 746
INTR_X86_SSSE3_PSHUF_B         = 747
INTR_X86_SSSE3_PSHUF_B_128     = 748
INTR_X86_SSSE3_PSIGN_B         = 749
INTR_X86_SSSE3_PSIGN_B_128     = 750
INTR_X86_SSSE3_PSIGN_D         = 751
INTR_X86_SSSE3_PSIGN_D_128     = 752
INTR_X86_SSSE3_PSIGN_W         = 753
INTR_X86_SSSE3_PSIGN_W_128     = 754
INTR_XCORE_BITREV              = 755
INTR_XCORE_GETID               = 756

