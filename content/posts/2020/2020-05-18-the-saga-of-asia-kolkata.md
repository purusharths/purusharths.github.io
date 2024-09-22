---
layout: post
title: "The Saga of Asia/Kolkata"
date: 2020-05-18 20:21
summary: Why Asia/Kolkata and not Asia/Mumbai or Asia/Delhi?
Tags: 
  - timezones
---

It's not really a saga for Asia/Kolkata (tzinfo). I just wondered why, even to this day, the Indian timezone is recognized by `Asia/Kolkata`. Even after Kolkata lost its status as the most populous or important city of India (there's no official benchmark for the latter, but with a bold claim we can say that if such a title exists it should go to either BOM, BLR, DEL, HYD, or MAA).

And as I looked into it, I found some interesting facts about IST (Full Disclosure: Citation Needed).

Long before IST, there was:

Time Zone             | Offset                | Abandoned in          | 
--------------------- | --------------------- | --------------------- | 
Calcutta Time         | UTC +5:53             | 1948			      | 
Madras Time           | UTC +5:21             |  -    				  |
Bombay Time           | UTC +4:51             | 1955     			  |

Madras Time was also called Railway time of India (since Madras Time lay between Calcutta and Bombay time) and of all the three, it was the closest to the current IST.

### So, why Asia/Kolkata?
Kolkata (then Calcutta) was the administrative capital of India and one of the most prominent city. The name Asia/Calcutta and later Asia/Kolkata was used since it was the most populous city in the zone at when the timezone was set up [1]. This is no longer true [2].

Technically, it should _have_ been changed, preferably to **Asia/Mumbai**.ia The last known conversation on this happened in 2012 and in 2015 [3][4]. 

```
Mayuresh Kathe mayuresh at wolfman.devio.us
Fri Dec 21 05:23:03 UTC 2012 

may i know the reason why asia/kolkata represents +0530 in india?
logically, technically and politically speaking, it's incorrect.

~mayuresh
```
and 
```
Sujay Phadke sujay.phadke at gmail.com
Thu Mar 5 00:08:29 UTC 2015 


Could you please add "New Delhi" or "Mumbai" to the +5:30 UTC timezone
list?
```

So, will the tzinfo be changed for India to Asia/Mumbai? It's unnecessary and unlikely. There can only be one zone representation for a country, and for all pratical purposes Asia/Kolkata does just that. It's a representation for the Indian Time Zone.

But given that Mumbai is the most populus city in India, should it be changed? The last answer on this topic answers the question for good and pretty much seals the fate of *Asia/Kolkata* [5]

```
Clive D.W. Feather clive at davros.org
Fri Mar 6 18:23:17 UTC 2015 

...
...

We don't need two names for the same zone.

I don't think we should make the change just because populations have
altered. That way lies madness as the most populous place keeps changing.
```

Moreover, the problems from updating the same the legacy systems from changing the tzinfo might cause an unnecessary overhead.


PS: [https://github.com/eggert/tz/blob/master/asia#L1263](https://github.com/eggert/tz/blob/master/asia#L1263)

---
### References:
[1] [https://mm.icann.org/pipermail/tz/2012-December/018487.html](https://mm.icann.org/pipermail/tz/2012-December/018487.html)<br>
[2] [http://pibmumbai.gov.in/scripts/detail.asp?releaseId=E2011IS3](https://web.archive.org/web/20150630112755/http://pibmumbai.gov.in/scripts/detail.asp?releaseId=E2011IS3) <br>
[3] [https://mm.icann.org/pipermail/tz/2012-December/018482.html](https://mm.icann.org/pipermail/tz/2012-December/018482.html)<br>
[4] [https://mm.icann.org/pipermail/tz/2015-March/022065.html](https://mm.icann.org/pipermail/tz/2015-March/022065.html) <br>
[5] [http://127.0.0.1:4000/misc/2020/05/18/the-saga-of-asia-kolkata.html](http://127.0.0.1:4000/misc/2020/05/18/the-saga-of-asia-kolkata.html)