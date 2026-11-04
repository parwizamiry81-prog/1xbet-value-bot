FOOTBALL INTELLIGENCE ENGINE

DATA GOVERNANCE, COLLECTION & VALIDATION STANDARD

استاندارد جامع جمع‌آوری، مدیریت و اعتبارسنجی داده‌های موتور هوشمند فوتبال

Project: Football Prediction & Intelligence Engine
Coverage: Europe's Top Five Football Leagues
Languages: Persian (فارسی) and English
Data Policy: Evidence-Based, Reproducible, Auditable
Status: Initial Data Architecture Specification

---

بخش اول: مأموریت و دامنه پروژه

PART I — PROJECT MISSION & SCOPE

1. Project Mission | مأموریت پروژه

فارسی:

هدف، توسعه یک سامانه جامع تحلیل و پیش‌بینی فوتبال با استفاده از داده‌های واقعی، قابل‌اعتماد، قابل‌ردیابی و قابل‌آزمایش است.

این سامانه باید بتواند عملکرد تیم‌ها و بازیکنان را تحلیل کند، شرایط پیش از مسابقه را ارزیابی کند، احتمال نتایج مختلف را محاسبه کند، پیش‌بینی منابع خارجی را ارزیابی کند و در صورت وجود اختلاف معنادار میان احتمال برآوردشده و احتمال بازار، فرصت احتمالی ارزش مورد انتظار مثبت (+EV) را شناسایی کند.

این پروژه نباید بر اساس حدس، اطلاعات ساختگی، شهرت تیم‌ها یا پیش‌بینی‌های بدون پشتوانه تصمیم بگیرد.

English:

The objective is to develop a comprehensive football intelligence and prediction system based on reliable, traceable, verifiable and testable data.

The system must analyze teams and players, evaluate pre-match conditions, estimate outcome probabilities, assess external predictions, and identify potential positive expected-value opportunities when a statistically justified difference exists between model probabilities and market probabilities.

No decision may rely on fabricated statistics, unsupported assumptions, team reputation alone, or unverified predictions.

2. Target Competitions | لیگ‌های تحت پوشش

The initial system covers:

1. English Premier League — لیگ برتر انگلیس
2. Spanish La Liga — لالیگا اسپانیا
3. German Bundesliga — بوندسلیگا آلمان
4. Italian Serie A — سری آ ایتالیا
5. French Ligue 1 — لیگ یک فرانسه

Each competition must have independent identifiers, historical records, season information and validation procedures.

هر لیگ باید شناسه، تاریخچه، فصل و فرآیند اعتبارسنجی مستقل داشته باشد.

---

بخش دوم: استاندارد داده‌های مسابقه

PART II — MATCH DATA STANDARD

3. Match Identification | شناسایی مسابقه

For every match, store:

- Unique match ID — شناسه یکتای مسابقه
- Competition ID — شناسه رقابت
- Season — فصل
- Matchday / Round — هفته مسابقات
- Match date — تاریخ مسابقه
- Kickoff time — ساعت شروع
- Time zone — منطقه زمانی
- Home team ID — شناسه تیم میزبان
- Away team ID — شناسه تیم مهمان
- Stadium — ورزشگاه
- Match status — وضعیت مسابقه
- Data provider — تأمین‌کننده داده
- Source URL — نشانی منبع
- Retrieval timestamp — زمان دریافت اطلاعات
- Last updated timestamp — زمان آخرین به‌روزرسانی

4. Match Results | نتایج مسابقات

When available, record:

- Half-time score — نتیجه نیمه اول
- Full-time score — نتیجه پایان بازی
- Extra-time score — نتیجه وقت اضافه
- Penalty shootout — نتیجه ضربات پنالتی
- Home goals — گل‌های میزبان
- Away goals — گل‌های مهمان
- Goal scorers — گل‌زنان
- Goal minutes — زمان گل‌ها
- Own goals — گل‌های به‌خودی
- Penalties — پنالتی‌ها
- Red cards — کارت‌های قرمز
- Yellow cards — کارت‌های زرد
- Substitutions — تعویض‌ها
- Referee — داور
- Attendance — تعداد تماشاگران

اطلاعاتی که در منبع وجود ندارند باید NULL باقی بمانند، نه اینکه تخمین زده شوند.

5. Match Events | رویدادهای مسابقه

Where available:

- Goals
- Assists
- Penalties
- Missed penalties
- Red cards
- Yellow cards
- Substitutions
- Injuries during match
- VAR decisions
- Own goals

هر رویداد باید دارای زمان، بازیکن مرتبط، مسابقه مرتبط و منبع اطلاعات باشد.

---

بخش سوم: تحلیل تیم‌ها

PART III — TEAM INTELLIGENCE

6. Team Performance | عملکرد تیم

For each team, calculate:

- Last 5 matches — پنج مسابقه اخیر
- Last 10 matches — ده مسابقه اخیر
- Season performance — عملکرد فصل
- Home performance — عملکرد خانگی
- Away performance — عملکرد خارج از خانه
- Wins, draws and losses — برد، مساوی و باخت
- Goals scored — گل زده
- Goals conceded — گل خورده
- Goal difference — تفاضل گل
- Clean sheets — کلین‌شیت
- Scoring consistency — ثبات گل‌زنی
- Defensive consistency — ثبات دفاعی
- First-half performance — عملکرد نیمه اول
- Second-half performance — عملکرد نیمه دوم
- Comeback performance — توان بازگشت به بازی
- Performance against strong opponents — عملکرد مقابل حریفان قدرتمند
- Performance against weak opponents — عملکرد مقابل حریفان ضعیف

7. Opponent Strength | قدرت حریفان قبلی

Previous results must be adjusted for opponent strength.

عوامل مورد بررسی:

- Opponent Elo rating
- Opponent league position
- Opponent offensive strength
- Opponent defensive strength
- Home or away context
- Competition strength
- Date and recency of the match

برد مقابل تیم ضعیف نباید هم‌ارزش برد مقابل تیم قدرتمند محسوب شود.

8. Team Tactical Analysis | تحلیل تاکتیکی

Where data is available:

- Formation — آرایش
- Possession style — سبک مالکیت توپ
- Pressing intensity — شدت پرس
- Defensive line — خط دفاع
- Counter-attacking ability — توان ضدحمله
- Build-up style — شیوه بازی‌سازی
- Width and attacking channels — عرض و مسیرهای حمله
- Set-piece strength — قدرت ضربات ایستگاهی
- Defensive transitions — انتقال دفاعی
- Offensive transitions — انتقال هجومی
- Tactical changes — تغییرات تاکتیکی
- Manager changes — تغییر مربی

Expected tactics and confirmed tactics must never be mixed.

---

بخش چهارم: تحلیل بازیکنان

PART IV — PLAYER INTELLIGENCE

9. Player Profiles | مشخصات بازیکنان

For every player:

- Unique player ID
- Full name
- Team
- Position
- Age, if available
- Preferred foot, if available
- Minutes played
- Starting appearances
- Substitute appearances
- Goals
- Assists
- Shots
- Shots on target
- Passing statistics
- Defensive statistics
- Recent performance
- Season performance

10. Advanced Player Metrics | آمار پیشرفته بازیکنان

When available:

- xG — گل مورد انتظار
- xA — پاس گل مورد انتظار
- xG per 90 minutes
- xA per 90 minutes
- Progressive passes
- Progressive carries
- Key passes
- Shot-creating actions
- Tackles
- Interceptions
- Pressures
- Aerial duels
- Expected threat (xT)

All metrics must retain their original provider definitions and units.

11. Player Availability | وضعیت حضور بازیکنان

Record:

- Confirmed injuries — مصدومیت تأییدشده
- Injury type — نوع مصدومیت
- Expected return — زمان احتمالی بازگشت
- Suspensions — محرومیت
- Fitness concerns — مشکلات آمادگی
- Confirmed availability — وضعیت تأییدشده حضور
- Uncertain availability — وضعیت نامشخص
- Expected absence impact — اثر احتمالی غیبت

هر خبر باید منبع و زمان انتشار داشته باشد. شایعه نباید به‌عنوان مصدومیت قطعی ثبت شود.

---

بخش پنجم: آمار پیشرفته مسابقه

PART V — ADVANCED MATCH STATISTICS

12. Team and Match Metrics | شاخص‌های تیمی و مسابقه‌ای

When available:

- Expected Goals (xG)
- Expected Goals Against (xGA)
- Expected Points (xPoints)
- Total shots
- Shots on target
- Big chances
- Big chances missed
- Possession
- Pass accuracy
- Corners
- Fouls
- Offsides
- Cards
- PPDA
- Field tilt
- Set-piece statistics

xG providers may use different models. Their values must not be treated as identical without validation.

---

بخش ششم: منابع فارسی و انگلیسی

PART VI — EXTERNAL PREDICTION SOURCES

13. Persian Sources | منابع فارسی‌زبان

Collect verifiable predictions from:

- Persian football websites
- Persian statistical analysts
- Persian sports publications
- Football experts
- Public prediction channels
- Match previews

14. English Sources | منابع انگلیسی‌زبان

Collect verifiable predictions from:

- Statistical prediction websites
- Football analytics platforms
- Professional analysts
- Sports publications
- Public expert previews
- Mathematical prediction models

15. Prediction Record | ثبت پیش‌بینی هر منبع

Each prediction must include:

- Source ID
- Source name
- Analyst name
- Language
- Match ID
- Prediction publication timestamp
- Collection timestamp
- Predicted outcome
- Home win probability
- Draw probability
- Away win probability
- Predicted score
- Over/Under prediction
- Both Teams To Score prediction
- Confidence level, if published
- Original source URL
- Archived source reference, where permitted

اگر منبع فقط گفته باشد «برد میزبان»، نباید احتمال عددی به آن نسبت داده شود.

---

بخش هفتم: موتور پیش‌بینی

PART VII — PREDICTION ENGINE

16. Statistical Models | مدل‌های آماری

The engine must support:

1. Poisson Regression
2. Dixon-Coles
3. Elo Rating
4. Time-decayed team strength
5. Home advantage estimation
6. Player availability adjustments
7. Expected goals models
8. Ensemble prediction models

Each model must be independently testable.

17. Prediction Outputs | خروجی پیش‌بینی

For each match:

- Home win probability
- Draw probability
- Away win probability
- Expected home goals
- Expected away goals
- Expected total goals
- Most likely scorelines
- Goal distribution
- Over/Under probabilities
- Both Teams To Score probability
- Model confidence and uncertainty
- Data completeness indicator
- Prediction timestamp

The three 1X2 probabilities must sum to 100%, subject only to rounding.

18. Prediction Scenarios | سناریوهای مسابقه

Generate scenarios such as:

- Low-scoring match
- High-scoring match
- Home dominance
- Away dominance
- Balanced match
- Early goal scenario
- Impact of a missing key player

Scenarios must be based on explicit assumptions and must not be presented as certain outcomes.

---

بخش هشتم: موتور ارزش مورد انتظار

PART VIII — EXPECTED VALUE ENGINE

19. Market Analysis | تحلیل بازار

Compare model probabilities with available market odds.

Calculate:

- Raw implied probability
- Overround
- No-vig probability
- Model probability
- Probability difference
- Expected value
- Expected return
- Odds movement
- Closing Line Value

20. +EV Decision Rules | قوانین تشخیص ارزش مثبت

A potential +EV signal must consider:

- Model calibration
- Minimum data quality
- Market liquidity, where available
- Odds timestamp
- Margin and commission
- Model uncertainty
- Probability estimation error

Positive EV is an estimate, not a guarantee of profit.

---

بخش نهم: ارزیابی علمی

PART IX — MODEL VALIDATION

21. Evaluation Metrics | معیارهای ارزیابی

Use:

- Brier Score
- Log Loss
- Calibration curves
- Reliability diagrams
- Accuracy
- Precision and recall, where appropriate
- ROI
- Closing Line Value

Accuracy alone is insufficient.

22. Backtesting | آزمون تاریخی

- Use chronological train/test separation.
- Never randomly mix future matches into past training data.
- Use rolling-origin validation.
- Compare with simple baseline models.
- Compare with market-implied probabilities.
- Report sample size and uncertainty intervals.
- Track performance separately by league and season.

23. No Guaranteed Accuracy | عدم تضمین دقت

The system must never claim guaranteed 99% accuracy.

Performance claims must be supported by reproducible out-of-sample testing.

هیچ درصد دقتی نباید بدون آزمایش مستقل و مستند اعلام شود.

---

بخش دهم: حاکمیت و اعتبار داده‌ها

PART X — DATA GOVERNANCE

24. Data Integrity | یکپارچگی داده

- Preserve original raw data.
- Validate JSON and CSV formats.
- Detect duplicate matches.
- Standardize team and player identifiers.
- Track missing values.
- Detect conflicting sources.
- Preserve source attribution.
- Record retrieval timestamps.
- Maintain data version history.
- Separate raw, cleaned and derived datasets.

25. Data Leakage Prevention | جلوگیری از نشت اطلاعات

Every prediction must use only information available before the prediction timestamp.

هر داده‌ای که بعد از زمان پیش‌بینی منتشر شده باشد، برای همان پیش‌بینی ممنوع است.

Historical predictions must be reproducible using the information available at the original cutoff time.

26. Missing Data Policy | سیاست داده‌های ناقص

- Never fabricate missing values.
- Never silently substitute estimates.
- Label estimated values explicitly.
- Preserve original missingness.
- Record imputation methods separately.
- Reduce confidence when critical information is unavailable.

27. Source Reliability | اعتبار منابع

Every provider must be evaluated for:

- Accuracy
- Completeness
- Update frequency
- Historical coverage
- Consistency
- Transparency
- Data availability
- Licensing and permitted usage

---

بخش یازدهم: منابع اولیه

PART XI — INITIAL DATA SOURCES

28. OpenFootball

Repository:

https://github.com/openfootball/football.json

Initial purpose:

- Historical fixtures
- Match dates
- Team names
- Match results
- Available lineups and match details

License: CC0-1.0, as stated by the repository.

OpenFootball must not be treated as a complete source for injuries, xG, advanced player metrics or live tactical information.

Additional providers must be researched and validated independently.

---

بخش دوازدهم: اصول اجرایی

PART XII — ENGINEERING PRINCIPLES

1. Accuracy over appearance — اعتبار بر ظاهر
2. Evidence over assumptions — شواهد بر حدس
3. Probability over certainty — احتمال بر قطعیت
4. Reproducibility over intuition — قابلیت بازتولید بر شهود
5. Data integrity over volume — صحت بر حجم داده
6. Independent validation — اعتبارسنجی مستقل
7. Transparent model limitations — شفافیت محدودیت‌ها
8. Continuous monitoring — پایش مستمر

Current Status: Specification only. No prediction model or validated database has been implemented yet.

وضعیت فعلی: این سند مشخصات پروژه است؛ هنوز موتور پیش‌بینی یا پایگاه داده اعتبارسنجی‌شده ساخته نشده است.