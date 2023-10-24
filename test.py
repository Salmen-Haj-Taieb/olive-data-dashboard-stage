import math
file=["16.07.22 07:03:07,63210025;1368;55;1657947600;32932;65472;0;42751;17;73;234;-3919;0;-310;0;-1313;0;32926;65472;726201;71157",
      "11.07.22 01:04:37,63210025;D01;55;1657486800;33363;65472;0;42751;17;52;262;-3920;0;-309;0;-1310;0;33345;65472;1575864;71173",
      "08.07.22 15:32:42,63210025;9F8;55;1657285200;32386;65472;0;42770;17;37;353;-3921;0;-307;0;-1305;0;32427;65472;1301142;71185",
      "23.07.22 11:03:15,63210025;1C28;55;1658566801;31799;65471;0;42780;17;55;338;-3919;0;-306;0;-1309;0;31786;65472;1685157;71361",
      "19.07.22 02:03:22,63210025;16D5;55;1658181600;32912;65472;0;42751;17;61;280;-3920;0;-308;0;-1311;0;33101;65472;1098734;71103",
      "09.07.22 08:04:03,63210025;AC5;55;1657339200;34212;65472;0;42751;17;59;239;-3920;0;-309;0;-1313;0;34075;65472;1289978;71242"

]
"""01.08.22 14:03:39,63210025;2710;55;1659308400;31309;65472;0;42751;17;64;289;-3918;0;-302;0;-1315;0;31353;65472;652415;71237",
      "01.08.22 12:03:35,63210025;26FB;55;1659304800;31309;65472;0;42751;17;59;295;-3918;0;-302;0;-1314;0;31270;65472;644877;71231",
      "01.08.22 11:14:37,621B0408;26F6;55;1659344400;29762;29251;55625;42566;17;49;324;-3773;0;-115;0;-1653;0;29616;26146;2598747;78968",
      "16.07.22 19:04:19,63210030;13F4;55;1657969200;30761;65472;0;43903;17;42;341;-4124;0;108;0;196;0;30735;65472;425502;71294",
      "16.07.22 03:03:49,63210030;1335;55;1657933200;31776;65472;0;43899;17;67;251;-4119;0;106;0;197;0;31758;65472;429501;71199",
      "11.07.22 22:03:52,63210030;E17;55;1657569600;33098;65472;0;43903;17;58;275;-4120;0;117;0;195;0;33044;65472;1092162;71213"""
data=[]

for x in file:
    L1=x.split()
    ch2=L1[1]
    L2=ch2.split(',')
    ch3=L2[1]
    L3=ch3.split(';')
    TDownStream_0=-7*(10**-11)*(int(L3[5]))**3 + 2*(10**-6)*(int(L3[5]))**2-0.0229*int(L3[5])+117.28
    TUpStream_0=-7*(10**-11)*(int(L3[6]))**3 + 2*(10**-6)*(int(L3[6]))**2-0.0229*int(L3[6])+117.28
    TDownStream_1=-7*(10**-11)*(int(L3[12]))**3 + 2*(10**-6)*(int(L3[12]))**2-0.0229*int(L3[12])+117.28
    TUpStream_1=-7*(10**-11)*(int(L3[13]))**3 + 2*(10**-6)*(int(L3[13]))**2-0.0229*int(L3[13])+117.28
    TDownStreamAvg=-7*(10**-11)*(int(L3[15]))**3 + 2*(10**-6)*(int(L3[15]))**2-0.0229*int(L3[15])+117.28
    TUpStreamAvg=-7*(10**-11)*(int(L3[16]))**3 + 2*(10**-6)*(int(L3[16]))**2-0.0229*int(L3[16])+117.28
    timeTdMax=(int(L3[19])*0.001)/3600
    timeTuMax=(int(L3[20])*0.001)/3600
    ΔTd_avg=((TDownStream_0-TDownStream_1)**2+40**2)**0.5
    ΔTu_avg=((TUpStream_0-TUpStream_1)**2+40**2)**0.5 #=40
    a=(math.log2(ΔTd_avg/ΔTu_avg)/0.5)**2
    b=(4/timeTdMax)
    c=(0.5/timeTdMax)**2
    data.append({"timeTdMax":timeTdMax,
                 "timeTuMax":timeTuMax,
                 "ΔTd_avg":ΔTd_avg,
                 "ΔTu_avg":ΔTu_avg,
                 "a":a,
                 "b":b,
                 "c":c
                })
print(data) 

"""15{
      0.036170819786814,
      0.035251978852883,
      0.037018994188337,
      0.035223000654072,
      0.035658392430306,
      

}

30{
      0.085833646626048,
      0.17982123339017,
      0.077895909777324,
      0.206810540412,
      0.08722881255372,
      0.19630598184534
}

25{
      0.11791071952744,
      0.054335695723248,
      0.065806228374771,
      0.05080989177172,
      0.077930104278786,
      0.06637761791691

}
"""
print((0.054335695723248+0.065806228374771+0.05080989177172+0.077930104278786+0.06637761791691)/5)