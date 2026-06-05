#!/usr/bin/env python3
import json

report_date = "2026-06-05 15:12"
entry_id = "mon-20260605-1512"

html = """<h1>AI&#x677F;&#x5757;&#x6536;&#x76D8;&#x76D1;&#x63A7;&#x62A5;&#x544A; &amp; COMEX&#x767D;&#x94F6;&#x671F;&#x8D27;&#x64AD;&#x62A5;</h1>
<p><strong>&#x62A5;&#x544A;&#x65F6;&#x95F4;&#xFF1A;2026-06-05 15:12</strong></p>
<p>&#x26A0;&#xFE0F; <strong>A&#x80A1;&#x4ECA;&#x65E5;&#xFF08;6&#x6708;5&#x65E5;&#xFF0C;&#x5468;&#x4E94;&#xFF09;&#x5DF2;&#x6536;&#x76D8;&#x3002;</strong>&#x4EE5;&#x4E0B;&#x4E3A;&#x4ECA;&#x65E5;&#x5168;&#x5929;&#x76D8;&#x9762;&#x56DE;&#x987E;&#x3001;&#x76D8;&#x540E;&#x6D88;&#x606F;&#x53CA;&#x4E0B;&#x5468;&#x5C55;&#x671B;&#x3002;</p>

<h2>&#x96F6;&#x3001;COMEX&#x767D;&#x94F6;&#x671F;&#x8D27;&#x64AD;&#x62A5;</h2>
<ul>
<li><strong>&#x6700;&#x65B0;&#x4EF7;&#x683C;&#xFF1A;</strong>COMEX&#x767D;&#x94F6;&#x671F;&#x8D27;&#x6700;&#x65B0;&#x62A5;&#x7EA6; <strong>73.06&#x7F8E;&#x5143;/&#x76CE;&#x53F8;</strong>&#xFF0C;&#x65E5;&#x5185;&#x8DCC;&#x7EA6; <strong>0.86%</strong>&#x3002;&#x5468;&#x56DB;&#x7EBD;&#x7EA6;&#x5C3E;&#x76D8;&#x62A5;74.16&#x7F8E;&#x5143;&#xFF08;&#x6DA8;1.69%&#xFF09;&#xFF0C;&#x4ECA;&#x65E5;&#x4E9A;&#x76D8;&#x51B2;&#x9AD8;&#x81F3;74.92&#x7F8E;&#x5143;&#x540E;&#x56DE;&#x843D;&#x3002;</li>
<li><strong>&#x73B0;&#x8D27;&#x767D;&#x94F6;&#xFF1A;</strong>&#x6700;&#x65B0;&#x62A5;73.89&#x7F8E;&#x5143;/&#x76CE;&#x53F8;&#x9644;&#x8FD1;&#x3002;&#x56FD;&#x5185;&#x4E0A;&#x91D1;&#x6240;&#x767D;&#x94F6;T+D&#x62A5;&#x7EA6;17,933&#x5143;/&#x5343;&#x514B;&#x3002;</li>
<li><strong>&#x8FD1;&#x671F;&#x8D8B;&#x52BF;&#xFF1A;</strong>&#x767D;&#x94F6;&#x81EA;5&#x6708;&#x4E2D;&#x65EC;&#x8FD1;90&#x7F8E;&#x5143;/&#x76CE;&#x53F8;&#x9AD8;&#x4F4D;&#x6301;&#x7EED;&#x56DE;&#x8C03;&#xFF0C;&#x76EE;&#x524D;&#x5728;<strong>72-76&#x7F8E;&#x5143;&#x533A;&#x95F4;&#x5BBD;&#x5E45;&#x9707;&#x8361;</strong>&#x3002;72&#x7F8E;&#x5143;&#x4E3A;&#x5173;&#x952E;&#x652F;&#x6491;&#xFF0C;76&#x7F8E;&#x5143;&#x4E3A;&#x77ED;&#x671F;&#x963B;&#x529B;&#x3002;</li>
<li><strong>&#x9A71;&#x52A8;&#x56E0;&#x7D20;&#x7B80;&#x6790;&#xFF1A;</strong>
<ul>
<li><strong>&#x7F8E;&#x5143;&#x6307;&#x6570;&#xFF1A;</strong>&#x4EA4;&#x6295;&#x4E8E;99.2&#x9644;&#x8FD1;&#xFF0C;&#x4ECE;&#x9AD8;&#x4F4D;&#x6709;&#x6240;&#x56DE;&#x843D;</li>
<li><strong>&#x7F8E;&#x8054;&#x50A8;&#x653F;&#x7B56;&#xFF1A;</strong>&#x7F8E;&#x56FD;5&#x6708;ADP&#x5C31;&#x4E1A;&#x8D85;&#x9884;&#x671F;&#xFF0C;&#x4ECA;&#x665A;<strong>20:30&#x5C06;&#x516C;&#x5E03;&#x975E;&#x519C;&#x6570;&#x636E;</strong>&#xFF0C;&#x4E3A;&#x77ED;&#x671F;&#x5173;&#x952E;&#x53D8;&#x91CF;</li>
<li><strong>&#x5DE5;&#x4E1A;&#x9700;&#x6C42;&#xFF1A;</strong>&#x5149;&#x4F0F;/&#x65B0;&#x80FD;&#x6E90;&#x6C7D;&#x8F66;/AI&#x786C;&#x4EF6;&#x7528;&#x94F6;&#x9700;&#x6C42;&#x7EF4;&#x6301;&#x9AD8;&#x4F4D;</li>
<li><strong>&#x5E93;&#x5B58;&#x652F;&#x6491;&#xFF1A;</strong>COMEX&#x767D;&#x94F6;&#x5E93;&#x5B58;&#x6301;&#x7EED;&#x4E0B;&#x964D;&#xFF0C;&#x5168;&#x7403;&#x4E3B;&#x8981;&#x4EA4;&#x6613;&#x6240;&#x5E93;&#x5B58;&#x5904;&#x4E8E;&#x8FD1;&#x5341;&#x5E74;&#x4F4E;&#x4F4D;</li>
</ul></li>
</ul>

<h2>&#x4E00;&#x3001;&#x5927;&#x76D8;&#x89E3;&#x8BFB;&#xFF08;6&#x6708;5&#x65E5;&#x6536;&#x76D8;&#x56DE;&#x987E;&#xFF09;</h2>
<ul>
<li><strong>&#x4E09;&#x5927;&#x6307;&#x6570;&#x4F4E;&#x5F00;&#x9AD8;&#x8D70;&#xFF0C;&#x6CA8;&#x6307;&#x6536;&#x6DA8;&#xFF1A;</strong>&#x4ECA;&#x65E5;A&#x80A1;&#x4E09;&#x5927;&#x6307;&#x6570;&#x96C6;&#x4F53;&#x4F4E;&#x5F00;&#xFF08;&#x6CA8;&#x6307;&#x8DCC;0.32%&#xFF09;&#xFF0C;&#x968F;&#x540E;&#x9707;&#x8361;&#x56DE;&#x5347;&#xFF0C;&#x4E0A;&#x8BC1;&#x6307;&#x6570;&#x6210;&#x529F;&#x7FFB;&#x7EA2;&#x3002;</li>
<li><strong>&#x9694;&#x591C;&#x5916;&#x56F4;&#x51B2;&#x51FB;&#xFF1A;</strong>&#x535A;&#x901A;Q3 AI&#x82AF;&#x7247;&#x6307;&#x5F15;160&#x4EBF;&#x7F8E;&#x5143;&#x4F4E;&#x4E8E;172&#x4EBF;&#x9884;&#x671F;&#xFF0C;<strong>&#x80A1;&#x4EF7;&#x66B4;&#x8DCC;12.59%</strong>&#xFF1B;&#x97E9;&#x56FD;&#x7EFC;&#x5408;&#x6307;&#x6570;&#x8DCC;&#x8D85;6%&#xFF0C;&#x4E09;&#x661F;&#x7535;&#x5B50;&#x8DCC;&#x8D85;6%&#xFF0C;SK&#x6D77;&#x529B;&#x58EB;&#x8DCC;&#x8D85;8%&#xFF0C;&#x97E9;&#x56FD;&#x4EA4;&#x6613;&#x6240;&#x542F;&#x52A8;&#x7194;&#x65AD;&#x673A;&#x5236;&#x300