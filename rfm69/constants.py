from enum import Enum


class Register(Enum):
    FIFO          = 0x00
    OPMODE          = 0x01
    DATAMODUL      = 0x02
    BITRATEMSB      = 0x03
    BITRATELSB      = 0x04
    FDEVMSB          = 0x05
    FDEVLSB          = 0x06
    FRFMSB          = 0x07
    FRFMID          = 0x08
    FRFLSB          = 0x09
    OSC1          = 0x0A
    AFCCTRL          = 0x0B
    LOWBAT          = 0x0C
    LISTEN1          = 0x0D
    LISTEN2          = 0x0E
    LISTEN3          = 0x0F
    VERSION          = 0x10
    PALEVEL          = 0x11
    PARAMP          = 0x12
    OCP              = 0x13
    AGCREF          = 0x14
    AGCTHRESH1      = 0x15
    AGCTHRESH2      = 0x16
    AGCTHRESH3      = 0x17
    LNA              = 0x18
    RXBW          = 0x19
    AFCBW          = 0x1A
    OOKPEAK          = 0x1B
    OOKAVG          = 0x1C
    OOKFIX          = 0x1D
    AFCFEI          = 0x1E
    AFCMSB          = 0x1F
    AFCLSB          = 0x20
    FEIMSB          = 0x21
    FEILSB          = 0x22
    RSSICONFIG      = 0x23
    RSSIVALUE      = 0x24
    DIOMAPPING1      = 0x25
    DIOMAPPING2      = 0x26
    IRQFLAGS1      = 0x27
    IRQFLAGS2      = 0x28
    RSSITHRESH      = 0x29
    RXTIMEOUT1      = 0x2A
    RXTIMEOUT2      = 0x2B
    PREAMBLEMSB      = 0x2C
    PREAMBLELSB      = 0x2D
    SYNCCONFIG      = 0x2E
    SYNCVALUE1      = 0x2F
    SYNCVALUE2      = 0x30
    SYNCVALUE3      = 0x31
    SYNCVALUE4      = 0x32
    SYNCVALUE5      = 0x33
    SYNCVALUE6      = 0x34
    SYNCVALUE7      = 0x35
    SYNCVALUE8      = 0x36
    PACKETCONFIG1  = 0x37
    PAYLOADLENGTH  = 0x38
    NODEADRS      = 0x39
    BROADCASTADRS  = 0x3A
    AUTOMODES      = 0x3B
    FIFOTHRESH      = 0x3C
    PACKETCONFIG2  = 0x3D
    AESKEY1          = 0x3E
    AESKEY2          = 0x3F
    AESKEY3          = 0x40
    AESKEY4          = 0x41
    AESKEY5          = 0x42
    AESKEY6          = 0x43
    AESKEY7          = 0x44
    AESKEY8          = 0x45
    AESKEY9          = 0x46
    AESKEY10      = 0x47
    AESKEY11      = 0x48
    AESKEY12      = 0x49
    AESKEY13      = 0x4A
    AESKEY14      = 0x4B
    AESKEY15      = 0x4C
    AESKEY16      = 0x4D
    TEMP1          = 0x4E
    TEMP2          = 0x4F
    TESTPA1          = 0x5A # only present on RFM69HW/SX1231H
    TESTPA2          = 0x5C # only present on RFM69HW/SX1231H
    TESTDAGC      = 0x6F
    TESTAFC       = 0x71


class RF(Enum):
    OPMODE_SEQUENCER_OFF                     = 0x80
    OPMODE_SEQUENCER_ON                      = 0x00 # Default

    OPMODE_LISTEN_ON                         = 0x40
    OPMODE_LISTEN_OFF                        = 0x00 # Default

    OPMODE_LISTENABORT                       = 0x20

    OPMODE_SLEEP                             = 0x00
    OPMODE_STANDBY                           = 0x04 # Default
    OPMODE_SYNTHESIZER                       = 0x08
    OPMODE_TRANSMITTER                       = 0x0C
    OPMODE_RECEIVER                          = 0x10

    # Reg Data Modul
    DATAMODUL_DATAMODE_PACKET                = 0x00 # Default
    DATAMODUL_DATAMODE_CONTINUOUS            = 0x40
    DATAMODUL_DATAMODE_CONTINUOUSNOBSYNC     = 0x60

    DATAMODUL_MODULATIONTYPE_FSK             = 0x00 # Default
    DATAMODUL_MODULATIONTYPE_OOK             = 0x08

    DATAMODUL_MODULATIONSHAPING_00           = 0x00 # Default
    DATAMODUL_MODULATIONSHAPING_01           = 0x01
    DATAMODUL_MODULATIONSHAPING_10           = 0x02
    DATAMODUL_MODULATIONSHAPING_11           = 0x03

    # RegBitRate (bits/sec) example bitrates
    BITRATEMSB_1200                          = 0x68
    BITRATELSB_1200                          = 0x2B
    BITRATEMSB_2400                          = 0x34
    BITRATELSB_2400                          = 0x15
    BITRATEMSB_4800                          = 0x1A # Default
    BITRATELSB_4800                          = 0x0B # Default
    BITRATEMSB_9600                          = 0x0D
    BITRATELSB_9600                          = 0x05
    BITRATEMSB_19200                         = 0x06
    BITRATELSB_19200                         = 0x83
    BITRATEMSB_38400                         = 0x03
    BITRATELSB_38400                         = 0x41
    BITRATEMSB_38323                         = 0x03
    BITRATELSB_38323                         = 0x43
    BITRATEMSB_34482                         = 0x03
    BITRATELSB_34482                         = 0xA0
    BITRATEMSB_76800                         = 0x01
    BITRATELSB_76800                         = 0xA1
    BITRATEMSB_153600                        = 0x00
    BITRATELSB_153600                        = 0xD0
    BITRATEMSB_57600                         = 0x02
    BITRATELSB_57600                         = 0x2C
    BITRATEMSB_115200                        = 0x01
    BITRATELSB_115200                        = 0x16
    BITRATEMSB_12500                         = 0x0A
    BITRATELSB_12500                         = 0x00
    BITRATEMSB_25000                         = 0x05
    BITRATELSB_25000                         = 0x00
    BITRATEMSB_50000                         = 0x02
    BITRATELSB_50000                         = 0x80
    BITRATEMSB_100000                        = 0x01
    BITRATELSB_100000                        = 0x40
    BITRATEMSB_150000                        = 0x00
    BITRATELSB_150000                        = 0xD5
    BITRATEMSB_200000                        = 0x00
    BITRATELSB_200000                        = 0xA0
    BITRATEMSB_250000                        = 0x00
    BITRATELSB_250000                        = 0x80
    BITRATEMSB_300000                        = 0x00
    BITRATELSB_300000                        = 0x6B
    BITRATEMSB_32768                         = 0x03
    BITRATELSB_32768                         = 0xD1
    # custom bitrates
    BITRATEMSB_55555                         = 0x02
    BITRATELSB_55555                         = 0x40
    BITRATEMSB_200KBPS                       = 0x00
    BITRATELSB_200KBPS                       = 0xa0

    # RegFdev - frequency deviation (Hz)
    FDEVMSB_2000                             = 0x00
    FDEVLSB_2000                             = 0x21
    FDEVMSB_5000                             = 0x00 # Default
    FDEVLSB_5000                             = 0x52 # Default
    FDEVMSB_7500                             = 0x00
    FDEVLSB_7500                             = 0x7B
    FDEVMSB_10000                            = 0x00
    FDEVLSB_10000                            = 0xA4
    FDEVMSB_15000                            = 0x00
    FDEVLSB_15000                            = 0xF6
    FDEVMSB_20000                            = 0x01
    FDEVLSB_20000                            = 0x48
    FDEVMSB_25000                            = 0x01
    FDEVLSB_25000                            = 0x9A
    FDEVMSB_30000                            = 0x01
    FDEVLSB_30000                            = 0xEC
    FDEVMSB_35000                            = 0x02
    FDEVLSB_35000                            = 0x3D
    FDEVMSB_40000                            = 0x02
    FDEVLSB_40000                            = 0x8F
    FDEVMSB_45000                            = 0x02
    FDEVLSB_45000                            = 0xE1
    FDEVMSB_50000                            = 0x03
    FDEVLSB_50000                            = 0x33
    FDEVMSB_55000                            = 0x03
    FDEVLSB_55000                            = 0x85
    FDEVMSB_60000                            = 0x03
    FDEVLSB_60000                            = 0xD7
    FDEVMSB_65000                            = 0x04
    FDEVLSB_65000                            = 0x29
    FDEVMSB_70000                            = 0x04
    FDEVLSB_70000                            = 0x7B
    FDEVMSB_75000                            = 0x04
    FDEVLSB_75000                            = 0xCD
    FDEVMSB_80000                            = 0x05
    FDEVLSB_80000                            = 0x1F
    FDEVMSB_85000                            = 0x05
    FDEVLSB_85000                            = 0x71
    FDEVMSB_90000                            = 0x05
    FDEVLSB_90000                            = 0xC3
    FDEVMSB_95000                            = 0x06
    FDEVLSB_95000                            = 0x14
    FDEVMSB_100000                           = 0x06
    FDEVLSB_100000                           = 0x66
    FDEVMSB_110000                           = 0x07
    FDEVLSB_110000                           = 0x0A
    FDEVMSB_120000                           = 0x07
    FDEVLSB_120000                           = 0xAE
    FDEVMSB_130000                           = 0x08
    FDEVLSB_130000                           = 0x52
    FDEVMSB_140000                           = 0x08
    FDEVLSB_140000                           = 0xF6
    FDEVMSB_150000                           = 0x09
    FDEVLSB_150000                           = 0x9A
    FDEVMSB_160000                           = 0x0A
    FDEVLSB_160000                           = 0x3D
    FDEVMSB_170000                           = 0x0A
    FDEVLSB_170000                           = 0xE1
    FDEVMSB_180000                           = 0x0B
    FDEVLSB_180000                           = 0x85
    FDEVMSB_190000                           = 0x0C
    FDEVLSB_190000                           = 0x29
    FDEVMSB_200000                           = 0x0C
    FDEVLSB_200000                           = 0xCD
    FDEVMSB_210000                           = 0x0D
    FDEVLSB_210000                           = 0x71
    FDEVMSB_220000                           = 0x0E
    FDEVLSB_220000                           = 0x14
    FDEVMSB_230000                           = 0x0E
    FDEVLSB_230000                           = 0xB8
    FDEVMSB_240000                           = 0x0F
    FDEVLSB_240000                           = 0x5C
    FDEVMSB_250000                           = 0x10
    FDEVLSB_250000                           = 0x00
    FDEVMSB_260000                           = 0x10
    FDEVLSB_260000                           = 0xA4
    FDEVMSB_270000                           = 0x11
    FDEVLSB_270000                           = 0x48
    FDEVMSB_280000                           = 0x11
    FDEVLSB_280000                           = 0xEC
    FDEVMSB_290000                           = 0x12
    FDEVLSB_290000                           = 0x8F
    FDEVMSB_300000                           = 0x13
    FDEVLSB_300000                           = 0x33

    # Reg Frf (MHz) - carrier frequency
    # 315 Mhz band
    FRFMSB_314                               = 0x4E
    FRFMID_314                               = 0x80
    FRFLSB_314                               = 0x00
    FRFMSB_315                               = 0x4E
    FRFMID_315                               = 0xC0
    FRFLSB_315                               = 0x00
    FRFMSB_316                               = 0x4F
    FRFMID_316                               = 0x00
    FRFLSB_316                               = 0x00
    # 433 mhz band
    FRFMSB_433                               = 0x6C
    FRFMID_433                               = 0x40
    FRFLSB_433                               = 0x00
    FRFMSB_434                               = 0x6C
    FRFMID_434                               = 0x80
    FRFLSB_434                               = 0x00
    FRFMSB_435                               = 0x6C
    FRFMID_435                               = 0xC0
    FRFLSB_435                               = 0x00
    # 868 Mhz band
    FRFMSB_863                               = 0xD7
    FRFMID_863                               = 0xC0
    FRFLSB_863                               = 0x00
    FRFMSB_864                               = 0xD8
    FRFMID_864                               = 0x00
    FRFLSB_864                               = 0x00
    FRFMSB_865                               = 0xD8
    FRFMID_865                               = 0x40
    FRFLSB_865                               = 0x00
    FRFMSB_866                               = 0xD8
    FRFMID_866                               = 0x80
    FRFLSB_866                               = 0x00
    FRFMSB_867                               = 0xD8
    FRFMID_867                               = 0xC0
    FRFLSB_867                               = 0x00
    FRFMSB_868                               = 0xD9
    FRFMID_868                               = 0x00
    FRFLSB_868                               = 0x00
    FRFMSB_869                               = 0xD9
    FRFMID_869                               = 0x40
    FRFLSB_869                               = 0x00
    FRFMSB_870                               = 0xD9
    FRFMID_870                               = 0x80
    FRFLSB_870                               = 0x00
    # 915 Mhz band
    FRFMSB_902                               = 0xE1
    FRFMID_902                               = 0x80
    FRFLSB_902                               = 0x00
    FRFMSB_903                               = 0xE1
    FRFMID_903                               = 0xC0
    FRFLSB_903                               = 0x00
    FRFMSB_904                               = 0xE2
    FRFMID_904                               = 0x00
    FRFLSB_904                               = 0x00
    FRFMSB_905                               = 0xE2
    FRFMID_905                               = 0x40
    FRFLSB_905                               = 0x00
    FRFMSB_906                               = 0xE2
    FRFMID_906                               = 0x80
    FRFLSB_906                               = 0x00
    FRFMSB_907                               = 0xE2
    FRFMID_907                               = 0xC0
    FRFLSB_907                               = 0x00
    FRFMSB_908                               = 0xE3
    FRFMID_908                               = 0x00
    FRFLSB_908                               = 0x00
    FRFMSB_909                               = 0xE3
    FRFMID_909                               = 0x40
    FRFLSB_909                               = 0x00
    FRFMSB_910                               = 0xE3
    FRFMID_910                               = 0x80
    FRFLSB_910                               = 0x00
    FRFMSB_911                               = 0xE3
    FRFMID_911                               = 0xC0
    FRFLSB_911                               = 0x00
    FRFMSB_912                               = 0xE4
    FRFMID_912                               = 0x00
    FRFLSB_912                               = 0x00
    FRFMSB_913                               = 0xE4
    FRFMID_913                               = 0x40
    FRFLSB_913                               = 0x00
    FRFMSB_914                               = 0xE4
    FRFMID_914                               = 0x80
    FRFLSB_914                               = 0x00
    FRFMSB_915                               = 0xE4 # Default
    FRFMID_915                               = 0xC0 # Default
    FRFLSB_915                               = 0x00 # Default
    FRFMSB_916                               = 0xE5
    FRFMID_916                               = 0x00
    FRFLSB_916                               = 0x00
    FRFMSB_917                               = 0xE5
    FRFMID_917                               = 0x40
    FRFLSB_917                               = 0x00
    FRFMSB_918                               = 0xE5
    FRFMID_918                               = 0x80
    FRFLSB_918                               = 0x00
    FRFMSB_919                               = 0xE5
    FRFMID_919                               = 0xC0
    FRFLSB_919                               = 0x00
    FRFMSB_920                               = 0xE6
    FRFMID_920                               = 0x00
    FRFLSB_920                               = 0x00
    FRFMSB_921                               = 0xE6
    FRFMID_921                               = 0x40
    FRFLSB_921                               = 0x00
    FRFMSB_922                               = 0xE6
    FRFMID_922                               = 0x80
    FRFLSB_922                               = 0x00
    FRFMSB_923                               = 0xE6
    FRFMID_923                               = 0xC0
    FRFLSB_923                               = 0x00
    FRFMSB_924                               = 0xE7
    FRFMID_924                               = 0x00
    FRFLSB_924                               = 0x00
    FRFMSB_925                               = 0xE7
    FRFMID_925                               = 0x40
    FRFLSB_925                               = 0x00
    FRFMSB_926                               = 0xE7
    FRFMID_926                               = 0x80
    FRFLSB_926                               = 0x00
    FRFMSB_927                               = 0xE7
    FRFMID_927                               = 0xC0
    FRFLSB_927                               = 0x00
    FRFMSB_928                               = 0xE8
    FRFMID_928                               = 0x00
    FRFLSB_928                               = 0x00

    # Reg Osc 1
    OSC1_RCCAL_START                         = 0x80
    OSC1_RCCAL_DONE                          = 0x40

    AFCLOWBETA_ON                            = 0x20
    AFCLOWBETA_OFF                           = 0x00 # Default

    # Reg Low Bat
    LOWBAT_MONITOR                           = 0x10
    LOWBAT_ON                                = 0x08
    LOWBAT_OFF                               = 0x00 # Default

    LOWBAT_TRIM_1695                         = 0x00
    LOWBAT_TRIM_1764                         = 0x01
    LOWBAT_TRIM_1835                         = 0x02 # Default
    LOWBAT_TRIM_1905                         = 0x03
    LOWBAT_TRIM_1976                         = 0x04
    LOWBAT_TRIM_2045                         = 0x05
    LOWBAT_TRIM_2116                         = 0x06
    LOWBAT_TRIM_2185                         = 0x07

    # Reg Listen 1
    LISTEN1_RESOL_64                         = 0x50
    LISTEN1_RESOL_4100                       = 0xA0 # Default
    LISTEN1_RESOL_262000                     = 0xF0

    LISTEN1_CRITERIA_RSSI                    = 0x00 # Default
    LISTEN1_CRITERIA_RSSIANDSYNC             = 0x08

    LISTEN1_END_00                           = 0x00
    LISTEN1_END_01                           = 0x02 # Default
    LISTEN1_END_10                           = 0x04

    # Reg Listen 2
    LISTEN2_COEFIDLE_VALUE                   = 0xF5 # Default

    # Reg Listen 3
    LISTEN3_COEFRX_VALUE                     = 0x20 # Default

    # Reg PaLevel
    PALEVEL_PA0_ON                           = 0x80 # Default
    PALEVEL_PA0_OFF                          = 0x00
    PALEVEL_PA1_ON                           = 0x40
    PALEVEL_PA1_OFF                          = 0x00 # Default
    PALEVEL_PA2_ON                           = 0x20
    PALEVEL_PA2_OFF                          = 0x00 # Default

    PALEVEL_OUTPUTPOWER_00000                = 0x00
    PALEVEL_OUTPUTPOWER_00001                = 0x01
    PALEVEL_OUTPUTPOWER_00010                = 0x02
    PALEVEL_OUTPUTPOWER_00011                = 0x03
    PALEVEL_OUTPUTPOWER_00100                = 0x04
    PALEVEL_OUTPUTPOWER_00101                = 0x05
    PALEVEL_OUTPUTPOWER_00110                = 0x06
    PALEVEL_OUTPUTPOWER_00111                = 0x07
    PALEVEL_OUTPUTPOWER_01000                = 0x08
    PALEVEL_OUTPUTPOWER_01001                = 0x09
    PALEVEL_OUTPUTPOWER_01010                = 0x0A
    PALEVEL_OUTPUTPOWER_01011                = 0x0B
    PALEVEL_OUTPUTPOWER_01100                = 0x0C
    PALEVEL_OUTPUTPOWER_01101                = 0x0D
    PALEVEL_OUTPUTPOWER_01110                = 0x0E
    PALEVEL_OUTPUTPOWER_01111                = 0x0F
    PALEVEL_OUTPUTPOWER_10000                = 0x10
    PALEVEL_OUTPUTPOWER_10001                = 0x11
    PALEVEL_OUTPUTPOWER_10010                = 0x12
    PALEVEL_OUTPUTPOWER_10011                = 0x13
    PALEVEL_OUTPUTPOWER_10100                = 0x14
    PALEVEL_OUTPUTPOWER_10101                = 0x15
    PALEVEL_OUTPUTPOWER_10110                = 0x16
    PALEVEL_OUTPUTPOWER_10111                = 0x17
    PALEVEL_OUTPUTPOWER_11000                = 0x18
    PALEVEL_OUTPUTPOWER_11001                = 0x19
    PALEVEL_OUTPUTPOWER_11010                = 0x1A
    PALEVEL_OUTPUTPOWER_11011                = 0x1B
    PALEVEL_OUTPUTPOWER_11100                = 0x1C
    PALEVEL_OUTPUTPOWER_11101                = 0x1D
    PALEVEL_OUTPUTPOWER_11110                = 0x1E
    PALEVEL_OUTPUTPOWER_11111                = 0x1F # Default

    # Reg PaRamp
    PARAMP_3400                              = 0x00
    PARAMP_2000                              = 0x01
    PARAMP_1000                              = 0x02
    PARAMP_500                               = 0x03
    PARAMP_250                               = 0x04
    PARAMP_125                               = 0x05
    PARAMP_100                               = 0x06
    PARAMP_62                                = 0x07
    PARAMP_50                                = 0x08
    PARAMP_40                                = 0x09 # Default
    PARAMP_31                                = 0x0A
    PARAMP_25                                = 0x0B
    PARAMP_20                                = 0x0C
    PARAMP_15                                = 0x0D
    PARAMP_12                                = 0x0E
    PARAMP_10                                = 0x0F

    # Reg Ocp
    OCP_OFF                                  = 0x0F
    OCP_ON                                   = 0x1A # Default

    OCP_TRIM_45                              = 0x00
    OCP_TRIM_50                              = 0x01
    OCP_TRIM_55                              = 0x02
    OCP_TRIM_60                              = 0x03
    OCP_TRIM_65                              = 0x04
    OCP_TRIM_70                              = 0x05
    OCP_TRIM_75                              = 0x06
    OCP_TRIM_80                              = 0x07
    OCP_TRIM_85                              = 0x08
    OCP_TRIM_90                              = 0x09
    OCP_TRIM_95                              = 0x0A
    OCP_TRIM_100                             = 0x0B # Default
    OCP_TRIM_105                             = 0x0C
    OCP_TRIM_110                             = 0x0D
    OCP_TRIM_115                             = 0x0E
    OCP_TRIM_120                             = 0x0F

    # Reg Agc Ref
    AGCREF_AUTO_ON                           = 0x40 # Default
    AGCREF_AUTO_OFF                          = 0x00

    AGCREF_LEVEL_MINUS80                     = 0x00 # Default
    AGCREF_LEVEL_MINUS81                     = 0x01
    AGCREF_LEVEL_MINUS82                     = 0x02
    AGCREF_LEVEL_MINUS83                     = 0x03
    AGCREF_LEVEL_MINUS84                     = 0x04
    AGCREF_LEVEL_MINUS85                     = 0x05
    AGCREF_LEVEL_MINUS86                     = 0x06
    AGCREF_LEVEL_MINUS87                     = 0x07
    AGCREF_LEVEL_MINUS88                     = 0x08
    AGCREF_LEVEL_MINUS89                     = 0x09
    AGCREF_LEVEL_MINUS90                     = 0x0A
    AGCREF_LEVEL_MINUS91                     = 0x0B
    AGCREF_LEVEL_MINUS92                     = 0x0C
    AGCREF_LEVEL_MINUS93                     = 0x0D
    AGCREF_LEVEL_MINUS94                     = 0x0E
    AGCREF_LEVEL_MINUS95                     = 0x0F
    AGCREF_LEVEL_MINUS96                     = 0x10
    AGCREF_LEVEL_MINUS97                     = 0x11
    AGCREF_LEVEL_MINUS98                     = 0x12
    AGCREF_LEVEL_MINUS99                     = 0x13
    AGCREF_LEVEL_MINUS100                    = 0x14
    AGCREF_LEVEL_MINUS101                    = 0x15
    AGCREF_LEVEL_MINUS102                    = 0x16
    AGCREF_LEVEL_MINUS103                    = 0x17
    AGCREF_LEVEL_MINUS104                    = 0x18
    AGCREF_LEVEL_MINUS105                    = 0x19
    AGCREF_LEVEL_MINUS106                    = 0x1A
    AGCREF_LEVEL_MINUS107                    = 0x1B
    AGCREF_LEVEL_MINUS108                    = 0x1C
    AGCREF_LEVEL_MINUS109                    = 0x1D
    AGCREF_LEVEL_MINUS110                    = 0x1E
    AGCREF_LEVEL_MINUS111                    = 0x1F
    AGCREF_LEVEL_MINUS112                    = 0x20
    AGCREF_LEVEL_MINUS113                    = 0x21
    AGCREF_LEVEL_MINUS114                    = 0x22
    AGCREF_LEVEL_MINUS115                    = 0x23
    AGCREF_LEVEL_MINUS116                    = 0x24
    AGCREF_LEVEL_MINUS117                    = 0x25
    AGCREF_LEVEL_MINUS118                    = 0x26
    AGCREF_LEVEL_MINUS119                    = 0x27
    AGCREF_LEVEL_MINUS120                    = 0x28
    AGCREF_LEVEL_MINUS121                    = 0x29
    AGCREF_LEVEL_MINUS122                    = 0x2A
    AGCREF_LEVEL_MINUS123                    = 0x2B
    AGCREF_LEVEL_MINUS124                    = 0x2C
    AGCREF_LEVEL_MINUS125                    = 0x2D
    AGCREF_LEVEL_MINUS126                    = 0x2E
    AGCREF_LEVEL_MINUS127                    = 0x2F
    AGCREF_LEVEL_MINUS128                    = 0x30
    AGCREF_LEVEL_MINUS129                    = 0x31
    AGCREF_LEVEL_MINUS130                    = 0x32
    AGCREF_LEVEL_MINUS131                    = 0x33
    AGCREF_LEVEL_MINUS132                    = 0x34
    AGCREF_LEVEL_MINUS133                    = 0x35
    AGCREF_LEVEL_MINUS134                    = 0x36
    AGCREF_LEVEL_MINUS135                    = 0x37
    AGCREF_LEVEL_MINUS136                    = 0x38
    AGCREF_LEVEL_MINUS137                    = 0x39
    AGCREF_LEVEL_MINUS138                    = 0x3A
    AGCREF_LEVEL_MINUS139                    = 0x3B
    AGCREF_LEVEL_MINUS140                    = 0x3C
    AGCREF_LEVEL_MINUS141                    = 0x3D
    AGCREF_LEVEL_MINUS142                    = 0x3E
    AGCREF_LEVEL_MINUS143                    = 0x3F

    # Reg Agc Thresh 1
    AGCTHRESH1_SNRMARGIN_000                 = 0x00
    AGCTHRESH1_SNRMARGIN_001                 = 0x20
    AGCTHRESH1_SNRMARGIN_010                 = 0x40
    AGCTHRESH1_SNRMARGIN_011                 = 0x60
    AGCTHRESH1_SNRMARGIN_100                 = 0x80
    AGCTHRESH1_SNRMARGIN_101                 = 0xA0 # Default
    AGCTHRESH1_SNRMARGIN_110                 = 0xC0
    AGCTHRESH1_SNRMARGIN_111                 = 0xE0

    AGCTHRESH1_STEP1_0                       = 0x00
    AGCTHRESH1_STEP1_1                       = 0x01
    AGCTHRESH1_STEP1_2                       = 0x02
    AGCTHRESH1_STEP1_3                       = 0x03
    AGCTHRESH1_STEP1_4                       = 0x04
    AGCTHRESH1_STEP1_5                       = 0x05
    AGCTHRESH1_STEP1_6                       = 0x06
    AGCTHRESH1_STEP1_7                       = 0x07
    AGCTHRESH1_STEP1_8                       = 0x08
    AGCTHRESH1_STEP1_9                       = 0x09
    AGCTHRESH1_STEP1_10                      = 0x0A
    AGCTHRESH1_STEP1_11                      = 0x0B
    AGCTHRESH1_STEP1_12                      = 0x0C
    AGCTHRESH1_STEP1_13                      = 0x0D
    AGCTHRESH1_STEP1_14                      = 0x0E
    AGCTHRESH1_STEP1_15                      = 0x0F
    AGCTHRESH1_STEP1_16                      = 0x10 # Default
    AGCTHRESH1_STEP1_17                      = 0x11
    AGCTHRESH1_STEP1_18                      = 0x12
    AGCTHRESH1_STEP1_19                      = 0x13
    AGCTHRESH1_STEP1_20                      = 0x14
    AGCTHRESH1_STEP1_21                      = 0x15
    AGCTHRESH1_STEP1_22                      = 0x16
    AGCTHRESH1_STEP1_23                      = 0x17
    AGCTHRESH1_STEP1_24                      = 0x18
    AGCTHRESH1_STEP1_25                      = 0x19
    AGCTHRESH1_STEP1_26                      = 0x1A
    AGCTHRESH1_STEP1_27                      = 0x1B
    AGCTHRESH1_STEP1_28                      = 0x1C
    AGCTHRESH1_STEP1_29                      = 0x1D
    AGCTHRESH1_STEP1_30                      = 0x1E
    AGCTHRESH1_STEP1_31                      = 0x1F

    # Reg Agc Thresh 2
    AGCTHRESH2_STEP2_0                       = 0x00
    AGCTHRESH2_STEP2_1                       = 0x10
    AGCTHRESH2_STEP2_2                       = 0x20
    AGCTHRESH2_STEP2_3                       = 0x30 # XXX wrong -- Default
    AGCTHRESH2_STEP2_4                       = 0x40
    AGCTHRESH2_STEP2_5                       = 0x50
    AGCTHRESH2_STEP2_6                       = 0x60
    AGCTHRESH2_STEP2_7                       = 0x70 # Default
    AGCTHRESH2_STEP2_8                       = 0x80
    AGCTHRESH2_STEP2_9                       = 0x90
    AGCTHRESH2_STEP2_10                      = 0xA0
    AGCTHRESH2_STEP2_11                      = 0xB0
    AGCTHRESH2_STEP2_12                      = 0xC0
    AGCTHRESH2_STEP2_13                      = 0xD0
    AGCTHRESH2_STEP2_14                      = 0xE0
    AGCTHRESH2_STEP2_15                      = 0xF0

    AGCTHRESH2_STEP3_0                       = 0x00
    AGCTHRESH2_STEP3_1                       = 0x01
    AGCTHRESH2_STEP3_2                       = 0x02
    AGCTHRESH2_STEP3_3                       = 0x03
    AGCTHRESH2_STEP3_4                       = 0x04
    AGCTHRESH2_STEP3_5                       = 0x05
    AGCTHRESH2_STEP3_6                       = 0x06
    AGCTHRESH2_STEP3_7                       = 0x07
    AGCTHRESH2_STEP3_8                       = 0x08
    AGCTHRESH2_STEP3_9                       = 0x09
    AGCTHRESH2_STEP3_10                      = 0x0A
    AGCTHRESH2_STEP3_11                      = 0x0B # Default
    AGCTHRESH2_STEP3_12                      = 0x0C
    AGCTHRESH2_STEP3_13                      = 0x0D
    AGCTHRESH2_STEP3_14                      = 0x0E
    AGCTHRESH2_STEP3_15                      = 0x0F

    # Reg Agc Thresh 3
    AGCTHRESH3_STEP4_0                       = 0x00
    AGCTHRESH3_STEP4_1                       = 0x10
    AGCTHRESH3_STEP4_2                       = 0x20
    AGCTHRESH3_STEP4_3                       = 0x30
    AGCTHRESH3_STEP4_4                       = 0x40
    AGCTHRESH3_STEP4_5                       = 0x50
    AGCTHRESH3_STEP4_6                       = 0x60
    AGCTHRESH3_STEP4_7                       = 0x70
    AGCTHRESH3_STEP4_8                       = 0x80
    AGCTHRESH3_STEP4_9                       = 0x90 # Default
    AGCTHRESH3_STEP4_10                      = 0xA0
    AGCTHRESH3_STEP4_11                      = 0xB0
    AGCTHRESH3_STEP4_12                      = 0xC0
    AGCTHRESH3_STEP4_13                      = 0xD0
    AGCTHRESH3_STEP4_14                      = 0xE0
    AGCTHRESH3_STEP4_15                      = 0xF0

    AGCTHRESH3_STEP5_0                       = 0x00
    AGCTHRESH3_STEP5_1                       = 0x01
    AGCTHRESH3_STEP5_2                       = 0x02
    AGCTHRESH3_STEP5_3                       = 0x03
    AGCTHRESH3_STEP5_4                       = 0x04
    AGCTHRESH3_STEP5_5                       = 0x05
    AGCTHRESH3_STEP5_6                       = 0x06
    AGCTHRESH3_STEP5_7                       = 0x07
    AGCTHRES33_STEP5_8                       = 0x08
    AGCTHRESH3_STEP5_9                       = 0x09
    AGCTHRESH3_STEP5_10                      = 0x0A
    AGCTHRESH3_STEP5_11                      = 0x0B # Default
    AGCTHRESH3_STEP5_12                      = 0x0C
    AGCTHRESH3_STEP5_13                      = 0x0D
    AGCTHRESH3_STEP5_14                      = 0x0E
    AGCTHRESH3_STEP5_15                      = 0x0F

    # Reg Lna
    LNA_ZIN_50                               = 0x00
    LNA_ZIN_200                              = 0x80 # Default

    LNA_LOWPOWER_OFF                         = 0x00 # Default
    LNA_LOWPOWER_ON                          = 0x40

    LNA_CURRENTGAIN                          = 0x08

    LNA_GAINSELECT_AUTO                      = 0x00 # Default
    LNA_GAINSELECT_MAX                       = 0x01
    LNA_GAINSELECT_MAXMINUS6                 = 0x02
    LNA_GAINSELECT_MAXMINUS12                = 0x03
    LNA_GAINSELECT_MAXMINUS24                = 0x04
    LNA_GAINSELECT_MAXMINUS36                = 0x05
    LNA_GAINSELECT_MAXMINUS48                = 0x06

    # Reg Rx Bw
    RXBW_DCCFREQ_000                         = 0x00
    RXBW_DCCFREQ_001                         = 0x20
    RXBW_DCCFREQ_010                         = 0x40 # Default
    RXBW_DCCFREQ_011                         = 0x60
    RXBW_DCCFREQ_100                         = 0x80
    RXBW_DCCFREQ_101                         = 0xA0
    RXBW_DCCFREQ_110                         = 0xC0
    RXBW_DCCFREQ_111                         = 0xE0

    RXBW_MANT_16                             = 0x00
    RXBW_MANT_20                             = 0x08
    RXBW_MANT_24                             = 0x10 # Default

    RXBW_EXP_0                               = 0x00
    RXBW_EXP_1                               = 0x01
    RXBW_EXP_2                               = 0x02
    RXBW_EXP_3                               = 0x03
    RXBW_EXP_4                               = 0x04
    RXBW_EXP_5                               = 0x05 # Default
    RXBW_EXP_6                               = 0x06
    RXBW_EXP_7                               = 0x07

    # Reg Afc Bw
    AFCBW_DCCFREQAFC_000                     = 0x00
    AFCBW_DCCFREQAFC_001                     = 0x20
    AFCBW_DCCFREQAFC_010                     = 0x40
    AFCBW_DCCFREQAFC_011                     = 0x60
    AFCBW_DCCFREQAFC_100                     = 0x80 # Default
    AFCBW_DCCFREQAFC_101                     = 0xA0
    AFCBW_DCCFREQAFC_110                     = 0xC0
    AFCBW_DCCFREQAFC_111                     = 0xE0

    AFCBW_MANTAFC_16                         = 0x00
    AFCBW_MANTAFC_20                         = 0x08 # Default
    AFCBW_MANTAFC_24                         = 0x10

    AFCBW_EXPAFC_0                           = 0x00
    AFCBW_EXPAFC_1                           = 0x01
    AFCBW_EXPAFC_2                           = 0x02
    AFCBW_EXPAFC_3                           = 0x03 # Default
    AFCBW_EXPAFC_4                           = 0x04
    AFCBW_EXPAFC_5                           = 0x05
    AFCBW_EXPAFC_6                           = 0x06
    AFCBW_EXPAFC_7                           = 0x07

    AFCFEI_AFCAUTO_ON                        = 0x04
    AFCFEI_AFCAUTO_OFF                       = 0x00

    AFCFEI_FEI_DONE                          = 0x40
    AFCFEI_FEI_START                         = 0x20
    AFCFEI_AFC_DONE                          = 0x10
    AFCFEI_AFCAUTOCLEAR_ON                   = 0x08
    AFCFEI_AFCAUTOCLEAR_OFF                  = 0x00

    # Reg Ook Peak
    OOKPEAK_THRESHTYPE_FIXED                 = 0x00
    OOKPEAK_THRESHTYPE_PEAK                  = 0x40 # Default
    OOKPEAK_THRESHTYPE_AVERAGE               = 0x80

    OOKPEAK_PEAKTHRESHSTEP_000               = 0x00 # Default
    OOKPEAK_PEAKTHRESHSTEP_001               = 0x08
    OOKPEAK_PEAKTHRESHSTEP_010               = 0x10
    OOKPEAK_PEAKTHRESHSTEP_011               = 0x18
    OOKPEAK_PEAKTHRESHSTEP_100               = 0x20
    OOKPEAK_PEAKTHRESHSTEP_101               = 0x28
    OOKPEAK_PEAKTHRESHSTEP_110               = 0x30
    OOKPEAK_PEAKTHRESHSTEP_111               = 0x38

    OOKPEAK_PEAKTHRESHDEC_000                = 0x00 # Default
    OOKPEAK_PEAKTHRESHDEC_001                = 0x01
    OOKPEAK_PEAKTHRESHDEC_010                = 0x02
    OOKPEAK_PEAKTHRESHDEC_011                = 0x03
    OOKPEAK_PEAKTHRESHDEC_100                = 0x04
    OOKPEAK_PEAKTHRESHDEC_101                = 0x05
    OOKPEAK_PEAKTHRESHDEC_110                = 0x06
    OOKPEAK_PEAKTHRESHDEC_111                = 0x07

    # Reg Ook Avg
    OOKAVG_AVERAGETHRESHFILT_00              = 0x00
    OOKAVG_AVERAGETHRESHFILT_01              = 0x40
    OOKAVG_AVERAGETHRESHFILT_10              = 0x80 # Default
    OOKAVG_AVERAGETHRESHFILT_11              = 0xC0

    # Reg Ook Fix
    OOKFIX_FIXEDTHRESH_VALUE                 = 0x06 # Default

    # Reg Afc Fei
    AFCFEI_FEI_DONE                          = 0x40
    AFCFEI_FEI_START                         = 0x20
    AFCFEI_AFC_DONE                          = 0x10
    AFCFEI_AFCAUTOCLEAR_ON                   = 0x08
    AFCFEI_AFCAUTOCLEAR_OFF                  = 0x00 # Default

    AFCFEI_AFCAUTO_ON                        = 0x04
    AFCFEI_AFCAUTO_OFF                       = 0x00 # Default

    AFCFEI_AFC_CLEAR                         = 0x02
    AFCFEI_AFC_START                         = 0x01

    # Reg Rssi Config
    RSSI_FASTRX_ON                           = 0x08
    RSSI_FASTRX_OFF                          = 0x00 # Default
    RSSI_DONE                                = 0x02
    RSSI_START                               = 0x01

    # Reg Dio Mapping 1
    DIOMAPPING1_DIO0_00                      = 0x00 # Default
    DIOMAPPING1_DIO0_01                      = 0x40
    DIOMAPPING1_DIO0_10                      = 0x80
    DIOMAPPING1_DIO0_11                      = 0xC0

    DIOMAPPING1_DIO1_00                      = 0x00 # Default
    DIOMAPPING1_DIO1_01                      = 0x10
    DIOMAPPING1_DIO1_10                      = 0x20
    DIOMAPPING1_DIO1_11                      = 0x30

    DIOMAPPING1_DIO2_00                      = 0x00 # Default
    DIOMAPPING1_DIO2_01                      = 0x04
    DIOMAPPING1_DIO2_10                      = 0x08
    DIOMAPPING1_DIO2_11                      = 0x0C

    DIOMAPPING1_DIO3_00                      = 0x00 # Default
    DIOMAPPING1_DIO3_01                      = 0x01
    DIOMAPPING1_DIO3_10                      = 0x02
    DIOMAPPING1_DIO3_11                      = 0x03

    # Reg Dio Mapping 2
    DIOMAPPING2_DIO4_00                      = 0x00 # Default
    DIOMAPPING2_DIO4_01                      = 0x40
    DIOMAPPING2_DIO4_10                      = 0x80
    DIOMAPPING2_DIO4_11                      = 0xC0

    DIOMAPPING2_DIO5_00                      = 0x00 # Default
    DIOMAPPING2_DIO5_01                      = 0x10
    DIOMAPPING2_DIO5_10                      = 0x20
    DIOMAPPING2_DIO5_11                      = 0x30

    DIOMAPPING2_CLKOUT_32                    = 0x00
    DIOMAPPING2_CLKOUT_16                    = 0x01
    DIOMAPPING2_CLKOUT_8                     = 0x02
    DIOMAPPING2_CLKOUT_4                     = 0x03
    DIOMAPPING2_CLKOUT_2                     = 0x04
    DIOMAPPING2_CLKOUT_1                     = 0x05
    DIOMAPPING2_CLKOUT_RC                    = 0x06
    DIOMAPPING2_CLKOUT_OFF                   = 0x07 # Default

    # Reg Irq Flags 1
    IRQFLAGS1_MODEREADY                      = 0x80
    IRQFLAGS1_RXREADY                        = 0x40
    IRQFLAGS1_TXREADY                        = 0x20
    IRQFLAGS1_PLLLOCK                        = 0x10
    IRQFLAGS1_RSSI                           = 0x08
    IRQFLAGS1_TIMEOUT                        = 0x04
    IRQFLAGS1_AUTOMODE                       = 0x02
    IRQFLAGS1_SYNCADDRESSMATCH               = 0x01

    # Reg Irq Flags 2
    IRQFLAGS2_FIFOFULL                       = 0x80
    IRQFLAGS2_FIFONOTEMPTY                   = 0x40
    IRQFLAGS2_FIFOLEVEL                      = 0x20
    IRQFLAGS2_FIFOOVERRUN                    = 0x10
    IRQFLAGS2_PACKETSENT                     = 0x08
    IRQFLAGS2_PAYLOADREADY                   = 0x04
    IRQFLAGS2_CRCOK                          = 0x02
    IRQFLAGS2_LOWBAT                         = 0x01

    # Reg Rssi Thresh
    RSSITHRESH_VALUE                         = 0xE4 # Default

    # Reg Rx Timeout 1
    RXTIMEOUT1_RXSTART_VALUE                 = 0x00 # Default

    # Reg Rx Timeout 2
    RXTIMEOUT2_RSSITHRESH_VALUE              = 0x00 # Default

    # Reg Preamble
    PREAMBLESIZE_MSB_VALUE                   = 0x00 # Default
    PREAMBLESIZE_LSB_VALUE                   = 0x03 # Default

    # Reg Sync Config
    SYNC_ON                                  = 0x80 # Default
    SYNC_OFF                                 = 0x00

    SYNC_FIFOFILL_AUTO                       = 0x00 # Default -- when sync interrupt occurs
    SYNC_FIFOFILL_MANUAL                     = 0x40

    SYNC_SIZE_1                              = 0x00
    SYNC_SIZE_2                              = 0x08
    SYNC_SIZE_3                              = 0x10
    SYNC_SIZE_4                              = 0x18 # Default
    SYNC_SIZE_5                              = 0x20
    SYNC_SIZE_6                              = 0x28
    SYNC_SIZE_7                              = 0x30
    SYNC_SIZE_8                              = 0x38

    SYNC_TOL_0                               = 0x00 # Default
    SYNC_TOL_1                               = 0x01
    SYNC_TOL_2                               = 0x02
    SYNC_TOL_3                               = 0x03
    SYNC_TOL_4                               = 0x04
    SYNC_TOL_5                               = 0x05
    SYNC_TOL_6                               = 0x06
    SYNC_TOL_7                               = 0x07

    # Reg Sync Value 1-8
    SYNC_BYTE1_VALUE                         = 0x00 # Default
    SYNC_BYTE2_VALUE                         = 0x00 # Default
    SYNC_BYTE3_VALUE                         = 0x00 # Default
    SYNC_BYTE4_VALUE                         = 0x00 # Default
    SYNC_BYTE5_VALUE                         = 0x00 # Default
    SYNC_BYTE6_VALUE                         = 0x00 # Default
    SYNC_BYTE7_VALUE                         = 0x00 # Default
    SYNC_BYTE8_VALUE                         = 0x00 # Default

    # Reg Packet Config 1
    PACKET1_FORMAT_FIXED                     = 0x00 # Default
    PACKET1_FORMAT_VARIABLE                  = 0x80

    PACKET1_DCFREE_OFF                       = 0x00 # Default
    PACKET1_DCFREE_MANCHESTER                = 0x20
    PACKET1_DCFREE_WHITENING                 = 0x40

    PACKET1_CRC_ON                           = 0x10 # Default
    PACKET1_CRC_OFF                          = 0x00

    PACKET1_CRCAUTOCLEAR_ON                  = 0x00 # Default
    PACKET1_CRCAUTOCLEAR_OFF                 = 0x08

    PACKET1_ADRSFILTERING_OFF                = 0x00 # Default
    PACKET1_ADRSFILTERING_NODE               = 0x02
    PACKET1_ADRSFILTERING_NODEBROADCAST      = 0x04

    # Reg Payload Length
    PAYLOADLENGTH_VALUE                      = 0x40 # Default

    # Reg Broadcast Adrs
    BROADCASTADDRESS_VALUE                   = 0x00

    # Reg Auto Modes
    AUTOMODES_ENTER_OFF                      = 0x00 # Default
    AUTOMODES_ENTER_FIFONOTEMPTY             = 0x20
    AUTOMODES_ENTER_FIFOLEVEL                = 0x40
    AUTOMODES_ENTER_CRCOK                    = 0x60
    AUTOMODES_ENTER_PAYLOADREADY             = 0x80
    AUTOMODES_ENTER_SYNCADRSMATCH            = 0xA0
    AUTOMODES_ENTER_PACKETSENT               = 0xC0
    AUTOMODES_ENTER_FIFOEMPTY                = 0xE0

    AUTOMODES_EXIT_OFF                       = 0x00 # Default
    AUTOMODES_EXIT_FIFOEMPTY                 = 0x04
    AUTOMODES_EXIT_FIFOLEVEL                 = 0x08
    AUTOMODES_EXIT_CRCOK                     = 0x0C
    AUTOMODES_EXIT_PAYLOADREADY              = 0x10
    AUTOMODES_EXIT_SYNCADRSMATCH             = 0x14
    AUTOMODES_EXIT_PACKETSENT                = 0x18
    AUTOMODES_EXIT_RXTIMEOUT                 = 0x1C

    AUTOMODES_INTERMEDIATE_SLEEP             = 0x00 # Default
    AUTOMODES_INTERMEDIATE_STANDBY           = 0x01
    AUTOMODES_INTERMEDIATE_RECEIVER          = 0x02
    AUTOMODES_INTERMEDIATE_TRANSMITTER       = 0x03

    #Reg Fifo Thresh
    FIFOTHRESH_TXSTART_FIFOTHRESH            = 0x00
    FIFOTHRESH_TXSTART_FIFONOTEMPTY          = 0x80 # Default

    FIFOTHRESH_VALUE                         = 0x0F # Default

    # Reg Packet Config 2
    PACKET2_RXRESTARTDELAY_1BIT              = 0x00 # Default
    PACKET2_RXRESTARTDELAY_2BITS             = 0x10
    PACKET2_RXRESTARTDELAY_4BITS             = 0x20
    PACKET2_RXRESTARTDELAY_8BITS             = 0x30
    PACKET2_RXRESTARTDELAY_16BITS            = 0x40
    PACKET2_RXRESTARTDELAY_32BITS            = 0x50
    PACKET2_RXRESTARTDELAY_64BITS            = 0x60
    PACKET2_RXRESTARTDELAY_128BITS           = 0x70
    PACKET2_RXRESTARTDELAY_256BITS           = 0x80
    PACKET2_RXRESTARTDELAY_512BITS           = 0x90
    PACKET2_RXRESTARTDELAY_1024BITS          = 0xA0
    PACKET2_RXRESTARTDELAY_2048BITS          = 0xB0
    PACKET2_RXRESTARTDELAY_NONE              = 0xC0
    PACKET2_RXRESTART                        = 0x04

    PACKET2_AUTORXRESTART_ON                 = 0x02 # Default
    PACKET2_AUTORXRESTART_OFF                = 0x00

    PACKET2_AES_ON                           = 0x01
    PACKET2_AES_OFF                          = 0x00 # Default

    # Reg Aes Key 1-16
    AESKEY1_VALUE                            = 0x00 # Default
    AESKEY2_VALUE                            = 0x00 # Default
    AESKEY3_VALUE                            = 0x00 # Default
    AESKEY4_VALUE                            = 0x00 # Default
    AESKEY5_VALUE                            = 0x00 # Default
    AESKEY6_VALUE                            = 0x00 # Default
    AESKEY7_VALUE                            = 0x00 # Default
    AESKEY8_VALUE                            = 0x00 # Default
    AESKEY9_VALUE                            = 0x00 # Default
    AESKEY10_VALUE                           = 0x00 # Default
    AESKEY11_VALUE                           = 0x00 # Default
    AESKEY12_VALUE                           = 0x00 # Default
    AESKEY13_VALUE                           = 0x00 # Default
    AESKEY14_VALUE                           = 0x00 # Default
    AESKEY15_VALUE                           = 0x00 # Default
    AESKEY16_VALUE                           = 0x00 # Default

    # Reg Temp 1
    TEMP1_MEAS_START                         = 0x08
    TEMP1_MEAS_RUNNING                       = 0x04
    TEMP1_ADCLOWPOWER_ON                     = 0x01 # Default
    TEMP1_ADCLOWPOWER_OFF                    = 0x00

    # Reg Test Dagc                             = 0x6F : demodulator config and IO mode config
    DAGC_NORMAL                              = 0x00 # Reset value
    DAGC_IMPROVED_LOWBETA1                   = 0x20 #
    DAGC_IMPROVED_LOWBETA0                   = 0x30 # Recommended default
