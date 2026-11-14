
NILE_N = [(32.53, 14.6), (32.53, 15.6), (32.67, 16.35), (33.2, 16.7), (33.7, 16.95), (33.98, 17.68), (33.95, 18.4), (33.6, 19.1), (33.32, 19.53), (32.7, 19.35), (32.2, 19.1), (31.8, 18.55), (30.95, 18.05), (30.6, 18.4), (30.48, 19.17), (30.42, 19.63), (30.35, 19.9), (30.6, 20.6), (30.9, 21.2), (31.33, 21.8), (31.62, 22.34), (32.0, 22.8), (32.6, 23.5), (32.9, 24.08), (32.9, 24.6)]

def nubiamap():
    k = 27.0; lon0, lon1, lat0, lat1 = 29.6, 34.6, 14.6, 24.6
    ox = 130
    P = lambda lon, lat: (round((lon - lon0) * k + ox, 1), round((lat1 - lat) * k + 34, 1))
    pts = ' '.join('%s,%s' % P(*p) for p in NILE_N)
    mw = (lon1 - lon0) * k; mh = (lat1 - lat0) * k; lx = ox + mw + 24
    W = int(lx + 190); H = int(mh + 58)
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of Nubia with the cataracts of the Nile">'
         f'<text x="{W/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Nubia: the land of the cataracts</text>'
         f'<rect x="{ox}" y="34" width="{mw}" height="{mh}" fill="#efe1bd"/>'
         f'<polyline points="{pts}" fill="none" stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/>')
    cats = [(32.9, 24.08, "1st"), (31.33, 21.8, "2nd"), (30.35, 19.9, "3rd"), (32.2, 19.1, "4th"), (33.95, 18.4, "5th"), (32.67, 16.35, "6th")]
    for lon, lat, n in cats:
        x, y = P(lon, lat)
        s += f'<path d="M{x-7} {y-3} l3.5 6 l3.5 -6 l3.5 6 l3.5 -6" fill="none" stroke="#DB2F30" stroke-width="2.2" transform="translate(0,0)"/><text x="{x-10}" y="{y+4}" text-anchor="end" font-size="10" font-weight="bold" fill="#DB2F30" style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">{n}</text>'
    marks = [(32.9, 24.08, "Aswan (ancient Egypt's southern border)"), (31.55, 22.15, 'Qustul (A-Group)'), (31.41, 21.95, 'Buhen'), (30.42, 19.6, 'Kerma'), (31.8, 18.55, 'Napata, Jebel Barkal'), (33.72, 16.93, 'Meroe'), (32.53, 15.6, 'Khartoum')]
    last = -99
    for lon, lat, lab in marks:
        x, y = P(lon, lat); ly = max(y, last + 19); last = ly
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="#0A1F3D" stroke="#fff"/><path d="M{x+5} {y} L{lx-4} {ly}" stroke="#8a8f99" stroke-width=".8"/><text x="{lx}" y="{ly+4}" font-size="11">{lab}</text>'
    for la, lb, t1, t2 in [(24.08, 21.8, 'LOWER NUBIA', 'Wawat'), (21.6, 15.0, 'UPPER NUBIA', 'Kush')]:
        y1 = P(0, la)[1]; y2 = P(0, lb)[1]; bx = ox - 10
        s += f'<path d="M{bx+6} {y1} h-6 v{y2-y1} h6" fill="none" stroke="#0A1F3D" stroke-width="2"/><text x="{bx-6}" y="{(y1+y2)/2-2}" text-anchor="end" font-weight="bold" font-size="11">{t1}</text><text x="{bx-6}" y="{(y1+y2)/2+12}" text-anchor="end" font-size="10">({t2})</text>'
    s += (f'<text x="{ox}" y="{H-6}" font-size="10" fill="#DB2F30">Red zigzags mark the six cataracts (rapids). The Nile flows north.</text></svg>')
    return s

def _tl():
    X = lambda y: round(60 + (4000 - y) * 0.13, 1)   # y = year BCE (negative = CE)
    def bar(a, b, row, c, t, fs=10, above=False):
        x, w = X(a), round(X(b) - X(a), 1); yy = 44 if row == 'n' else 132
        lab = (f'<text x="{x+w/2}" y="{yy-4 if row=="n" else yy+36}" text-anchor="middle" font-size="10" font-weight="bold" fill="{c}">{t}</text>' if above
               else f'<text x="{x+w/2}" y="{yy+15}" text-anchor="middle" fill="#fff" font-size="{fs}">{t}</text>')
        return f'<rect x="{x}" y="{yy}" width="{w}" height="22" rx="3" fill="{c}"/>' + lab
    s = ('<svg viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Timeline of Nubia and Kemet">'
         '<text x="320" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Two neighbors, thousands of years of history</text>'
         '<text x="8" y="60" font-weight="bold" fill="#8a6d1f" font-size="10">NUBIA</text><text x="8" y="148" font-weight="bold" fill="#0047BA" font-size="10">KEMET</text>'
         f'<line x1="{X(4000)}" y1="104" x2="{X(-50)}" y2="104" stroke="#0A1F3D" stroke-width="2"/>')
    for y, t in [(4000, "4000 BCE"), (3000, "3000"), (2000, "2000"), (1000, "1000"), (0, "1 CE")]:
        s += f'<line x1="{X(y)}" y1="100" x2="{X(y)}" y2="108" stroke="#0A1F3D"/><text x="{X(y)}" y="121" text-anchor="middle" font-size="10">{t}</text>'
    s += bar(3800, 2900, 'n', '#C9A84C', 'A-Group') + bar(2500, 1500, 'n', '#C9A84C', 'Kerma: first Kush')
    s += bar(1500, 1070, 'n', '#8a6d1f', 'Egypt rules', 9) + bar(900, -50, 'n', '#C9A84C', 'Napata, then Meroe')
    s += f'<rect x="{X(750)}" y="72" width="{round(X(664)-X(750),1)}" height="18" rx="3" fill="#DB2F30"/><text x="{X(664)+5}" y="85" font-size="10" font-weight="bold" fill="#DB2F30">25th Dynasty</text>'
    s += bar(3900, 3100, 'k', '#0047BA', 'Badarian and Naqada') + bar(2686, 1650, 'k', '#0047BA', 'Old to Middle Kingdom')
    s += bar(1550, 1070, 'k', '#0047BA', 'New Kingdom', 9) + bar(750, 664, 'k', '#DB2F30', 'Kush rules', above=True) + bar(664, 332, 'k', '#0047BA', 'Late', 9)
    s += ('<text x="320" y="196" text-anchor="middle" font-size="11">The red bars line up: from about 750 to 664 BCE, kings from Kush ruled both lands.</text>'
          '<text x="320" y="212" text-anchor="middle" font-size="10" fill="#5b6676">Bars are approximate. Gaps are periods of division between the kingdoms.</text></svg>')
    return s

TIMELINE = _tl()

DEFFUFA = ('<svg viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="The Western Deffufa at Kerma">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The Western Deffufa: a mud-brick temple at Kerma</text>'
  '<rect x="0" y="178" width="560" height="30" fill="#e3c99a"/>'
  '<path d="M124 178 L148 70 L412 70 L436 178Z" fill="#b8763e" stroke="#7a4a1f" stroke-width="2"/>'
  + ''.join(f'<line x1="{round(150-24*(10+j*12)/108,1)}" y1="{80+j*12}" x2="{round(410+24*(10+j*12)/108,1)}" y2="{80+j*12}" stroke="#7a4a1f" stroke-width=".7"/>' for j in range(8)) +
  '<rect x="262" y="134" width="36" height="44" fill="#5a3a1a"/>'
    '<g fill="#0A1F3D"><circle cx="100" cy="170" r="3"/><rect x="98" y="173" width="4" height="6"/></g><text x="100" y="196" text-anchor="middle" font-size="10">a person, to scale</text>'
  '<path d="M466 70 v108" stroke="#DB2F30"/><path d="M462 70 h8 M462 178 h8" stroke="#DB2F30"/><text x="476" y="118" font-size="11">about 18 m</text><text x="476" y="133" font-size="11">(60 ft) tall</text>'
  '<text x="280" y="232" text-anchor="middle" font-size="11">Built of sun-dried mud brick. Its base is about 52 m by 27 m. Still standing after more than 3,500 years.</text></svg>')

LESSON = {'unit': 'Unit 2: The Nile Valley and Ancient Africa',
 'title': 'Nubia and the Kingdom of Kush',
 'subtitle': "South of Egypt lay a rich land of gold, archers and powerful kings. For thousands of years, Nubia was Egypt's partner, rival and sometimes its ruler.",
 'objectives': ['Locate Nubia, its cataracts, and the sites of Qustul, Kerma and Napata on a map.',
                'Describe the A-Group culture and explain the debate over the Qustul incense burner.',
                'Explain how the Kingdom of Kerma (the first Kush) grew rich and powerful, and what the Western Deffufa shows.',
                "Use the Sobeknakht inscription as evidence of Kush's military power.",
                'Describe the changing relationship between Kush and Egypt: trade, war, conquest and independence.'],
 'vocab': [['Nubia', "The region along the Nile south of Egypt, in today's southern Egypt and northern Sudan."],
           ['Kush', 'The name Egyptians used for the kingdoms of Upper Nubia, including Kerma and later Napata and Meroe.'],
           ['Ta-Seti', '"Land of the Bow," an Egyptian name for Nubia and for Egypt\'s southernmost region, honoring Nubian archers.'],
           ['cataract', 'A rocky stretch of rapids in the Nile. Nubia lies along the six cataracts.'],
           ['deffufa', "A Nubian word for a huge mud-brick building; the Western Deffufa was Kerma's great temple."],
           ['trade route', 'A path used by traders to carry goods between places.'],
           ['tribute', 'Payment or goods that a weaker ruler or people must give to a more powerful one.'],
           ['independence', 'Freedom from control by another country.']],
 'reconnect': {'title': 'Week 7: Kemet as an African civilization',
               'intro': "Nubia was Kemet's closest African neighbor. Review last week's evidence first.",
               'items': [{'t': 'text',
                          'q': 'Week 7: ancient Egyptian belongs to which large language family, shared with Hausa, Somali and Amharic?',
                          'a': ['afroasiatic', 'afro-asiatic', 'afro asiatic'],
                          'show': 'Afroasiatic',
                          'pts': 2,
                          'why': 'Afroasiatic. Most of its branches are spoken in Africa, one more sign that Kemet was African.'},
                         {'t': 'open',
                          'key': 'rc_lower',
                          'q': 'Week 7 said early Upper Egyptian cultures were closely related to the cultures of Lower Nubia. What does that suggest about how Egypt and Nubia began?',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['They shared roots or grew from related peoples and traditions'],
                          'model': 'It suggests that Egypt and Nubia grew from related peoples who shared traditions like pottery and cattle herding, so they began as neighbors with common roots.'},
                         {'t': 'open',
                          'key': 'rc_bias',
                          'q': 'Why did some writers in the 1800s want to cut Egypt out of African history and deny that it was a Black African civilization?',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Racism; to claim Black Africans could not build civilizations; to justify colonialism and slavery'],
                          'model': 'They held racist beliefs that Black Africans could not build great civilizations, and that idea helped them justify colonialism and slavery.'},
                         {'t': 'blanks',
                          'q': 'Complete the sentence.',
                          'sent': 'The 25th Dynasty of Egypt was ruled by kings from ___.',
                          'blanks': [['kush', 'nubia']],
                          'show': 'Kush',
                          'pts': 2,
                          'why': 'Week 7 previewed that kings from Kush ruled all of Egypt as the 25th Dynasty.'}]},
 'hook': {'title': 'The Land of the Bow',
          'visual': '<svg viewBox="0 0 479 328" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of Nubia with the cataracts of the Nile"><text '
                    'x="239.5" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Nubia: the land of the cataracts</text><rect x="130" y="34" width="135.0" '
                    'height="270.00000000000006" fill="#efe1bd"/><polyline points="209.1,304.0 209.1,277.0 212.9,256.8 227.2,247.3 240.7,240.6 248.3,220.8 247.5,201.4 238.0,182.5 230.4,170.9 '
                    '213.7,175.8 200.2,182.5 189.4,197.4 166.4,210.9 157.0,201.4 153.8,180.6 152.1,168.2 150.2,160.9 157.0,142.0 165.1,125.8 176.7,109.6 184.5,95.0 194.8,82.6 211.0,63.7 219.1,48.0 '
                    '219.1,34.0" fill="none" stroke="#0047BA" stroke-width="3" stroke-linejoin="round"/><path d="M212.1 45.0 l3.5 6 l3.5 -6 l3.5 6 l3.5 -6" fill="none" stroke="#DB2F30" '
                    'stroke-width="2.2" transform="translate(0,0)"/><text x="209.1" y="52.0" text-anchor="end" font-size="10" font-weight="bold" fill="#DB2F30" '
                    'style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">1st</text><path d="M169.7 106.6 l3.5 6 l3.5 -6 l3.5 6 l3.5 -6" fill="none" stroke="#DB2F30" stroke-width="2.2" '
                    'transform="translate(0,0)"/><text x="166.7" y="113.6" text-anchor="end" font-size="10" font-weight="bold" fill="#DB2F30" '
                    'style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">2nd</text><path d="M143.2 157.9 l3.5 6 l3.5 -6 l3.5 6 l3.5 -6" fill="none" stroke="#DB2F30" stroke-width="2.2" '
                    'transform="translate(0,0)"/><text x="140.2" y="164.9" text-anchor="end" font-size="10" font-weight="bold" fill="#DB2F30" '
                    'style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">3rd</text><path d="M193.2 179.5 l3.5 6 l3.5 -6 l3.5 6 l3.5 -6" fill="none" stroke="#DB2F30" stroke-width="2.2" '
                    'transform="translate(0,0)"/><text x="190.2" y="186.5" text-anchor="end" font-size="10" font-weight="bold" fill="#DB2F30" '
                    'style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">4th</text><path d="M240.5 198.4 l3.5 6 l3.5 -6 l3.5 6 l3.5 -6" fill="none" stroke="#DB2F30" stroke-width="2.2" '
                    'transform="translate(0,0)"/><text x="237.5" y="205.4" text-anchor="end" font-size="10" font-weight="bold" fill="#DB2F30" '
                    'style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">5th</text><path d="M205.9 253.8 l3.5 6 l3.5 -6 l3.5 6 l3.5 -6" fill="none" stroke="#DB2F30" stroke-width="2.2" '
                    'transform="translate(0,0)"/><text x="202.9" y="260.8" text-anchor="end" font-size="10" font-weight="bold" fill="#DB2F30" '
                    'style="paint-order:stroke;stroke:#efe1bd;stroke-width:3">6th</text><circle cx="219.1" cy="48.0" r="4" fill="#0A1F3D" stroke="#fff"/><path d="M224.1 48.0 L285.0 48.0" '
                    'stroke="#8a8f99" stroke-width=".8"/><text x="289.0" y="52.0" font-size="11">Aswan (ancient Egypt\'s southern border)</text><circle cx="182.6" cy="100.2" r="4" fill="#0A1F3D" '
                    'stroke="#fff"/><path d="M187.6 100.2 L285.0 100.2" stroke="#8a8f99" stroke-width=".8"/><text x="289.0" y="104.2" font-size="11">Qustul (A-Group)</text><circle cx="178.9" '
                    'cy="105.6" r="4" fill="#0A1F3D" stroke="#fff"/><path d="M183.9 105.6 L285.0 119.2" stroke="#8a8f99" stroke-width=".8"/><text x="289.0" y="123.2" '
                    'font-size="11">Buhen</text><circle cx="152.1" cy="169.0" r="4" fill="#0A1F3D" stroke="#fff"/><path d="M157.1 169.0 L285.0 169.0" stroke="#8a8f99" stroke-width=".8"/><text '
                    'x="289.0" y="173.0" font-size="11">Kerma</text><circle cx="189.4" cy="197.4" r="4" fill="#0A1F3D" stroke="#fff"/><path d="M194.4 197.4 L285.0 197.4" stroke="#8a8f99" '
                    'stroke-width=".8"/><text x="289.0" y="201.4" font-size="11">Napata, Jebel Barkal</text><circle cx="241.2" cy="241.1" r="4" fill="#0A1F3D" stroke="#fff"/><path d="M246.2 241.1 '
                    'L285.0 241.1" stroke="#8a8f99" stroke-width=".8"/><text x="289.0" y="245.1" font-size="11">Meroe</text><circle cx="209.1" cy="277.0" r="4" fill="#0A1F3D" stroke="#fff"/><path '
                    'd="M214.1 277.0 L285.0 277.0" stroke="#8a8f99" stroke-width=".8"/><text x="289.0" y="281.0" font-size="11">Khartoum</text><path d="M126 48.0 h-6 v61.599999999999994 h6" '
                    'fill="none" stroke="#0A1F3D" stroke-width="2"/><text x="114" y="76.8" text-anchor="end" font-weight="bold" font-size="11">LOWER NUBIA</text><text x="114" y="90.8" '
                    'text-anchor="end" font-size="10">(Wawat)</text><path d="M126 115.0 h-6 v178.2 h6" fill="none" stroke="#0A1F3D" stroke-width="2"/><text x="114" y="202.1" text-anchor="end" '
                    'font-weight="bold" font-size="11">UPPER NUBIA</text><text x="114" y="216.1" text-anchor="end" font-size="10">(Kush)</text><text x="130" y="322" font-size="10" fill="#DB2F30">Red '
                    'zigzags mark the six cataracts (rapids). The Nile flows north.</text></svg>',
          'html': '<p>Travel up the Nile from Kemet (Egypt) past Aswan and the river changes. Granite boulders break the water into rapids called <b>cataracts</b>, and golden desert presses close to '
                  'a narrow green strip. This is <b>Nubia</b>. The Nubians were Black Africans, and Nubian peoples still live along the Nile in southern Egypt and northern Sudan today, many still '
                  'speaking Nubian languages.</p><p>The Egyptians called it <b>Ta-Seti</b>, "the Land of the Bow," because Nubian archers were famous for their skill. Egyptian armies hired Nubian '
                  'archers, and models of Nubian archers marching in formation were placed in Egyptian tombs. Nubia was also rich in gold, ivory, ebony and incense, goods that flowed north to Egypt '
                  "and beyond.</p><div class='callout'><b>Big idea:</b> Nubia was not Egypt's shadow. It built its own kingdoms, with its own capitals, religion, art and armies, and at times it was "
                  'the stronger power.</div>'},
 'learn': [{'title': 'The A-Group and the Qustul Debate',
            'html': '<p>From about 3800 to 2900 BCE, a farming and trading people archaeologists call the <b>A-Group</b> lived in Lower Nubia. They traded ivory, ebony and incense from the south for '
                    'Egyptian goods. At <b>Qustul</b>, archaeologists found royal tombs filled with gold and fine pottery, showing that powerful rulers lived there.</p><p>In one damaged tomb lay a '
                    "carved stone <b>incense burner</b> from around 3200 BCE. It shows a king wearing a tall crown like Egypt's White Crown, seated in a boat, with a falcon above a palace façade. In "
                    "1980, archaeologist <b>Bruce Williams</b> argued that it showed Nubian kings using royal symbols as early as, or earlier than, Egypt's first kings, and that kingship might have "
                    "begun in Nubia.</p><p>Most archaeologists disagree. They point to Egyptian royal symbols found at Abydos that are older, and argue that Qustul's rulers borrowed Egyptian "
                    "symbols, or that the burner itself was made in Egypt. Williams later said he meant only that Egypt's first royal family may have had roots near Qustul. The debate is still "
                    'discussed. Today most Egyptologists think the Egyptian symbols came first, but scholars still debate what Qustul shows about early Nubian kingship. Either way, Qustul shows that '
                    'Nubia had kings and wealth at the very dawn of the Nile kingdoms. Today the Qustul cemeteries lie under Lake Nasser, flooded by the Aswan High Dam. When the lake filled in the '
                    '1960s, more than 100,000 Nubians had to leave their villages. An international rescue campaign moved some temples, such as Abu Simbel, but many sites, including Qustul, were '
                    'flooded.</p>',
            'checks': [{'t': 'open',
                        'key': 'qustul',
                        'q': 'Explain the two sides of the debate over the Qustul incense burner. What does the object prove, no matter which side is right?',
                        'min': 35,
                        'rows': 4,
                        'rubric': ['Williams: Nubian kings used royal symbols as early as or earlier than Egypt; kingship might have begun in Nubia',
                                   'Others: older Egyptian symbols exist; Qustul rulers borrowed them, or the burner was made in Egypt and imported',
                                   'Either way, Nubia had powerful kings and wealth about 3200 BCE'],
                        'model': 'Bruce Williams argued the burner shows Nubian kings using royal symbols as early as or earlier than Egypt, so kingship might have started in Nubia. Other '
                                 "archaeologists say older Egyptian symbols exist, so Qustul's rulers borrowed them. Either way, it proves Nubia had powerful kings and great wealth around 3200 BCE."},
                       {'t': 'open',
                        'key': 'lakenasser',
                        'q': 'The Qustul cemeteries now lie under Lake Nasser (called Lake Nubia in Sudan). Besides ancient sites, what did the lake cost Nubian people, and why does that loss matter '
                             'to historians?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['More than 100,000 Nubians lost their homes and villages', 'Flooded sites like Qustul can no longer be studied, so evidence of Nubian history is lost'],
                        'model': 'More than 100,000 Nubians had to leave their villages, and sites like Qustul were flooded. Historians lost evidence they can never dig up again, and Nubian families '
                                 'lost places tied to their own history.'}]},
           {'title': 'Kerma: The First Kingdom of Kush',
            'visual': '<svg viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="The Western Deffufa at Kerma"><text x="280" y="18" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">The Western Deffufa: a mud-brick temple at Kerma</text><rect x="0" y="178" width="560" height="30" '
                      'fill="#e3c99a"/><path d="M124 178 L148 70 L412 70 L436 178Z" fill="#b8763e" stroke="#7a4a1f" stroke-width="2"/><line x1="147.8" y1="80" x2="412.2" y2="80" stroke="#7a4a1f" '
                      'stroke-width=".7"/><line x1="145.1" y1="92" x2="414.9" y2="92" stroke="#7a4a1f" stroke-width=".7"/><line x1="142.4" y1="104" x2="417.6" y2="104" stroke="#7a4a1f" '
                      'stroke-width=".7"/><line x1="139.8" y1="116" x2="420.2" y2="116" stroke="#7a4a1f" stroke-width=".7"/><line x1="137.1" y1="128" x2="422.9" y2="128" stroke="#7a4a1f" '
                      'stroke-width=".7"/><line x1="134.4" y1="140" x2="425.6" y2="140" stroke="#7a4a1f" stroke-width=".7"/><line x1="131.8" y1="152" x2="428.2" y2="152" stroke="#7a4a1f" '
                      'stroke-width=".7"/><line x1="129.1" y1="164" x2="430.9" y2="164" stroke="#7a4a1f" stroke-width=".7"/><rect x="262" y="134" width="36" height="44" fill="#5a3a1a"/><g '
                      'fill="#0A1F3D"><circle cx="100" cy="170" r="3"/><rect x="98" y="173" width="4" height="6"/></g><text x="100" y="196" text-anchor="middle" font-size="10">a person, to '
                      'scale</text><path d="M466 70 v108" stroke="#DB2F30"/><path d="M462 70 h8 M462 178 h8" stroke="#DB2F30"/><text x="476" y="118" font-size="11">about 18 m</text><text x="476" '
                      'y="133" font-size="11">(60 ft) tall</text><text x="280" y="232" text-anchor="middle" font-size="11">Built of sun-dried mud brick. Its base is about 52 m by 27 m. Still '
                      'standing after more than 3,500 years.</text></svg>',
            'html': '<p>By about 2500 BCE, the city of <b>Kerma</b>, near the Third Cataract, became the capital of a powerful kingdom. Egyptians called it <b>Kush</b>. At its height, about 1750 to '
                    "1580 BCE, Kerma's kings controlled the Nile from the First Cataract to the Fifth, a stretch longer than Egypt itself.</p><p>At the center of Kerma stood the <b>Western "
                    'Deffufa</b>, a giant mud-brick temple that still towers over the town today. The kings were buried under enormous round mounds, some about 90 meters across, with treasures and '
                    'many attendants. Kerma traded gold, ivory, ebony, cattle and incense, and its potters made thin, polished black-and-red beakers famous for their quality.</p><p>Kerma had no '
                    "writing of its own that we know of, so much of what we know comes from archaeology. Egyptian texts also mention Kush, but they were written from Egypt's point of view. Swiss "
                    'archaeologist <b>Charles Bonnet</b> excavated Kerma for decades, beginning in the 1970s, and showed it was a true African city with palaces, temples and neighborhoods, not just '
                    'an outpost of Egypt as early researchers assumed.</p>',
            'checks': [{'t': 'open',
                        'key': 'kermarich',
                        'q': 'Give two reasons Kerma became rich and powerful. Use details from the lesson.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Control of the Nile and trade routes between Egypt and the south', 'Valuable goods: gold, ivory, ebony, incense, cattle'],
                        'model': 'Kerma controlled a long stretch of the Nile, so goods from central Africa had to pass through it on the way to Egypt. It also had valuable resources like gold, '
                                 'ivory, ebony and cattle to trade.'},
                       {'t': 'open',
                        'key': 'nowriting',
                        'q': 'Kerma left no written records of its own. How do historians learn about a people without writing? Name two kinds of evidence and what each can tell us.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Archaeology: buildings, tombs, pottery show wealth, beliefs, skills', 'Records written by neighbors (Egyptian texts), with their bias'],
                        'model': "Archaeology, like the Deffufa, the royal mounds and the pottery, shows Kerma's wealth, religion and skill. Egyptian texts that mention Kush tell about wars and "
                                 "trade, but they show Egypt's point of view, so historians compare them with the archaeology."},
                       {'t': 'num',
                        'q': "The Western Deffufa's base is about 52 meters by 27 meters. About how many square meters does it cover?",
                        'a': 1404,
                        'tol': 1,
                        'unit': 'square meters',
                        'pts': 3,
                        'why': '52 × 27 = 1,404 square meters, about a quarter of an American football field.'}]},
           {'title': 'When Kush Struck Egypt',
            'html': "<p>Around 1650 to 1550 BCE, Egypt was weak and divided. Kush grew stronger. For a long time, historians knew little about Kush's role. Then in 2003, British Egyptologists "
                    'cleaning the tomb of <b>Sobeknakht</b>, an Egyptian governor at Elkab in Upper Egypt, found a 22-line inscription painted in red.</p><p>The inscription describes a huge army '
                    "from Kush and its allies, including Medjay warriors from the eastern desert, attacking deep into Egypt. Sobeknakht boasts about the Egyptian counterattack. The British Museum's "
                    'Vivian Davies, who studied it, explained that it shows Kush was powerful enough to invade Egypt, something Egyptian records had kept quiet.</p><p>Egypt struck back. Around 1500 '
                    'BCE, King Thutmose I led armies south and conquered Kerma, and later kings destroyed the city and ruled Nubia for about 400 years. Egypt took Nubian gold, and the sons of Nubian '
                    "rulers were raised at the Egyptian court. Paintings in the tomb of Huy, Tutankhamun's governor of Kush, show Nubian princes bringing gold and other tribute, and a Nubian "
                    'princess riding in a chariot pulled by oxen. Yet Nubians kept their identity, and when Egypt weakened again around 1070 BCE, Kush became independent once more.</p>',
            'checks': [{'t': 'open',
                        'key': 'sobek',
                        'q': "Why might Egyptian records have said little about Kush's invasion of Egypt? What does the Sobeknakht inscription teach about the bias of sources?",
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Royal records celebrated victories and hid defeats', "Sources reflect their makers' point of view; new evidence can change history"],
                        'model': 'Egyptian kings wanted to look powerful, so official records celebrated victories and kept quiet about defeats. The Sobeknakht inscription shows that sources reflect '
                                 'who made them, and that a new discovery can change what historians know.'},
                       {'t': 'num',
                        'q': "How many years passed between Kush's attack (about 1575 BCE) and the inscription's discovery in 2003 CE?",
                        'a': [3578, 3577],
                        'unit': 'years',
                        'show': 'about 3,577 years (3,578 by simple adding)',
                        'pts': 3,
                        'why': '1,575 + 2,003 = 3,578, or 3,577 because there is no year 0.'},
                       {'t': 'open',
                        'key': 'tribute',
                        'q': 'Look at what happened after Egypt conquered Kush. Give one way Egypt changed Nubia and one way Nubians kept their own identity.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Egypt took gold, collected tribute, raised Nubian princes in Egypt, built temples',
                                   'Nubians kept their identity and later regained independence (around 1070 BCE)'],
                        'model': "Egypt took Nubia's gold and raised the sons of Nubian rulers at the Egyptian court. But Nubians kept their own identity, and when Egypt weakened around 1070 BCE, "
                                 'Kush became independent again.'}]},
           {'title': 'Kush Rises Again: Napata',
            'visual': '<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Timeline of Nubia and Kemet"><text x="280" y="18" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Two neighbors, thousands of years of history</text><text x="20" y="58" font-weight="bold" '
                      'fill="#C9A84C">NUBIA</text><text x="20" y="148" font-weight="bold" fill="#0047BA">KEMET</text><line x1="70" y1="100" x2="540" y2="100" stroke="#0A1F3D" stroke-width="2"/><line '
                      'x1="70" y1="96" x2="70" y2="104" stroke="#0A1F3D"/><text x="70" y="116" text-anchor="middle" font-size="10">4000 BCE</text><line x1="180" y1="96" x2="180" y2="104" '
                      'stroke="#0A1F3D"/><text x="180" y="116" text-anchor="middle" font-size="10">3000</text><line x1="290" y1="96" x2="290" y2="104" stroke="#0A1F3D"/><text x="290" y="116" '
                      'text-anchor="middle" font-size="10">2000</text><line x1="400" y1="96" x2="400" y2="104" stroke="#0A1F3D"/><text x="400" y="116" text-anchor="middle" '
                      'font-size="10">1000</text><line x1="510" y1="96" x2="510" y2="104" stroke="#0A1F3D"/><text x="510" y="116" text-anchor="middle" font-size="10">1 CE</text><rect x="92" y="44" '
                      'width="99" height="22" rx="4" fill="#C9A84C"/><text x="141.5" y="59" text-anchor="middle" fill="#fff" font-size="10">A-Group</text><rect x="235" y="44" width="110" height="22" '
                      'rx="4" fill="#C9A84C"/><text x="290.0" y="59" text-anchor="middle" fill="#fff" font-size="10">Kerma: first Kush</text><rect x="345" y="70" width="55" height="22" rx="4" '
                      'fill="#8a6d1f"/><text x="372.5" y="85" text-anchor="middle" fill="#fff" font-size="10">Egypt rules</text><rect x="416" y="44" width="32" height="22" rx="4" '
                      'fill="#DB2F30"/><text x="432.0" y="59" text-anchor="middle" fill="#fff" font-size="10">25th</text><rect x="402" y="70" width="120" height="22" rx="4" fill="#C9A84C"/><text '
                      'x="462.0" y="85" text-anchor="middle" fill="#fff" font-size="10">Napata, then Meroe</text><rect x="70" y="130" width="125" height="22" rx="4" fill="#0047BA"/><text x="132.5" '
                      'y="145" text-anchor="middle" fill="#fff" font-size="10">Badarian and Naqada</text><rect x="214" y="130" width="113" height="22" rx="4" fill="#0047BA"/><text x="270.5" y="145" '
                      'text-anchor="middle" fill="#fff" font-size="10">Old to Middle Kingdom</text><rect x="337" y="130" width="63" height="22" rx="4" fill="#0047BA"/><text x="368.5" y="145" '
                      'text-anchor="middle" fill="#fff" font-size="10">New Kingdom</text><rect x="416" y="130" width="32" height="22" rx="4" fill="#DB2F30"/><text x="432.0" y="145" '
                      'text-anchor="middle" fill="#fff" font-size="10">Kush</text><rect x="448" y="130" width="74" height="22" rx="4" fill="#0047BA"/><text x="485.0" y="145" text-anchor="middle" '
                      'fill="#fff" font-size="10">Later Egypt</text><text x="280" y="186" text-anchor="middle" font-size="11">The red bars line up: around 750 to 664 BCE, kings from Kush ruled both '
                      'lands.</text><text x="280" y="202" text-anchor="middle" font-size="10" fill="#5b6676">Bars are approximate.</text></svg>',
            'html': '<p>After Egyptian rule ended, a new Kushite kingdom grew at <b>Napata</b>, beside a flat-topped sandstone mountain called <b>Jebel Barkal</b>, near the Fourth Cataract. Kushites '
                    'and Egyptians both believed the god Amun lived inside this "Pure Mountain," so it became one of the holiest places in the Nile Valley.</p><p>Kush\'s rulers built temples, kept '
                    'many Egyptian religious traditions and wrote in Egyptian hieroglyphs, while keeping Nubian customs in burial, dress and kingship. By about 750 BCE, Kush was strong enough to '
                    "march north, and its kings would soon rule all of Egypt as the <b>25th Dynasty</b>. That is next week's story.</p>",
            'checks': [{'t': 'open',
                        'key': 'barkal',
                        'q': 'Why was Jebel Barkal important to both Kushites and Egyptians?',
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Both believed Amun lived inside the mountain', "Made Napata a holy center that gave Kush's kings religious authority"],
                        'model': "Both peoples believed the god Amun lived inside Jebel Barkal, so the mountain was sacred. That made Napata a holy center and gave Kush's kings special religious "
                                 'authority.'},
                       {'t': 'open',
                        'key': 'exchange',
                        'q': 'Kush borrowed Egyptian gods and hieroglyphs but kept Nubian burial customs and kingship. Earlier, Egypt borrowed from Nubia, too. Why do neighboring cultures borrow '
                             'from each other, and does borrowing mean one culture is less important?',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Contact through trade, marriage, war leads to sharing ideas', 'Borrowing does not make a culture less important; all cultures borrow and adapt'],
                        'model': 'Neighbors trade, marry and fight, so ideas travel both ways. Borrowing does not make a culture less important. Kush adapted Egyptian ideas in its own way, just as '
                                 'Egypt took Nubian archers, gold and traditions.'},
                       {'t': 'order',
                        'q': 'Put these events in time order, earliest first.',
                        'items': ['A-Group rulers are buried with royal symbols at Qustul',
                                  'Kerma becomes the capital of the first Kingdom of Kush',
                                  'Kush and its allies attack deep into Egypt',
                                  'Thutmose I conquers Kerma',
                                  'Kush becomes independent again as Egypt weakens',
                                  "Kush's kings march north to rule Egypt as the 25th Dynasty"],
                        'pts': 4,
                        'why': 'About 3200, 2500, 1575, 1500, 1070 and 750 BCE.'}]}],
 'handson': {'title': "Make Mud Bricks Like Kerma's Builders",
             'intro': 'The Western Deffufa has stood for more than 3,500 years, and it is made of mud. Test how builders made mud brick strong.',
             'materials': ['Soil with some clay in it (garden soil works), about 4 cups',
                           'Water',
                           'Dry grass, straw or shredded paper',
                           'An ice cube tray, small paper cups or a muffin tin as molds',
                           'A bowl and a spoon',
                           'A sunny spot to dry the bricks for several days',
                           'A ruler and a few books for a strength test'],
             'steps': ['Make two mixtures: soil and water only, and soil, water and a handful of dry grass or straw mixed in.',
                       'Press each mixture firmly into molds and label them A (no straw) and B (with straw).',
                       'Let them dry in the sun for 3 to 5 days, then pop them out.',
                       'Strength test: place a brick across two books, set more books on top one at a time, and record how many it holds before it cracks.',
                       'Drop test: drop one brick of each kind from 30 cm onto grass and record what happens.'],
             'record': [{'t': 'open',
                         'key': 'brickdata',
                         'q': 'Record your results in a table: brick type, number of books held, and what happened in the drop test. Which brick was stronger?',
                         'min': 30,
                         'rows': 5,
                         'rubric': ['Data table for both brick types', 'Clear comparison', 'Identifies the stronger brick'],
                         'model': 'Brick A (no straw): held 3 books, broke into pieces in the drop test. Brick B (with straw): held 6 books, chipped but stayed whole. Brick B was stronger.'},
                        {'t': 'open',
                         'key': 'brickwhy',
                         'q': "Explain why adding straw might make mud brick stronger, and why a dry climate like Nubia's helped the Western Deffufa last so long.",
                         'min': 30,
                         'rows': 3,
                         'rubric': ['Straw fibers hold the mud together and stop cracks spreading', 'Little rain means less erosion, so mud brick survives'],
                         'model': 'The straw fibers act like a net that holds the dried mud together, so cracks do not spread as easily. Nubia gets very little rain, so the mud bricks were not '
                                  'washed away, which is why the Deffufa still stands.'}]},
 'think': {'intro': 'Use evidence and explain your reasoning. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'neighbors',
                      'q': 'Write a paragraph explaining how the relationship between Kush and Egypt changed over time. Include at least four events or periods, in order, and explain what caused one '
                           'of the changes.',
                      'min': 110,
                      'rows': 10,
                      'rubric': ['Four or more accurate events or periods in chronological order',
                                 'Explains a cause of one change',
                                 'Shows the relationship went both ways (trade, war, conquest, independence)',
                                 'Clear organization with transitions'],
                      'model': 'The relationship between Kush and Egypt changed many times over 3,000 years. Around 3200 BCE, the A-Group rulers of Qustul traded with Egypt and shared royal symbols. '
                               "Later, from about 2500 BCE, the Kingdom of Kerma grew rich by controlling trade along the Nile. Around 1575 BCE, while Egypt was weak and divided, Kush's army "
                               'attacked deep into Egypt, as the Sobeknakht inscription shows. Egypt struck back around 1500 BCE: Thutmose I conquered Kerma, and Egypt ruled Nubia for about 400 '
                               'years, taking its gold. When Egypt weakened around 1070 BCE, Kush became independent again, and by about 750 BCE its kings marched north to rule Egypt. One cause of '
                               'these changes was the balance of power: whenever one kingdom was divided or weak, the other grew stronger and expanded.'},
                     {'t': 'open',
                      'key': 'textbook',
                      'q': "Many older textbooks mention Nubia only as a place Egypt conquered. Using this week's evidence, write two sentences a better textbook should include about Nubia, and "
                           'explain why including them matters.',
                      'min': 45,
                      'rows': 5,
                      'rubric': ["Two accurate, specific sentences (Kerma's power, the Sobeknakht invasion, Qustul kings, independence)",
                                 'Explains why a fuller story matters (accuracy, fairness, African history)'],
                      'model': '1. The Kingdom of Kerma ruled the Nile from the First to the Fifth Cataract and around 1575 BCE was strong enough to invade Egypt. 2. Kush regained its independence '
                               'and later ruled all of Egypt as the 25th Dynasty. Including these facts matters because leaving them out makes African kingdoms seem weaker than they were and tells '
                               "only Egypt's side of the story."}]},
 'exit': [{'t': 'text',
           'q': 'What does Ta-Seti mean?',
           'a': ['land of the bow', 'land of bow', 'bow land'],
           'show': 'the Land of the Bow',
           'pts': 2,
           'why': 'Nubian archers were famous for their skill and served in Egyptian armies.'},
          {'t': 'open',
           'key': 'exit_deffufa',
           'q': 'What was the Western Deffufa, and what does it show about Kerma?',
           'min': 12,
           'rows': 2,
           'rubric': ['A huge mud-brick temple at Kerma', 'Shows wealth, organization and skilled builders'],
           'model': "It was Kerma's giant mud-brick temple. It shows that Kerma was a rich, organized city with skilled builders and its own religion."},
          {'t': 'open',
           'key': 'exit_sobek',
           'q': 'What did the Sobeknakht inscription, found in 2003, reveal?',
           'min': 10,
           'rows': 2,
           'rubric': ['Kush and its allies invaded deep into Egypt (about 1575 to 1550 BCE)'],
           'model': 'It revealed that an army from Kush and its allies invaded deep into Egypt around 1575 to 1550 BCE.'},
          {'t': 'text', 'q': 'Which Kushite capital stood beside Jebel Barkal, the "Pure Mountain"?', 'a': ['napata'], 'show': 'Napata', 'pts': 2, 'why': 'Napata, near the Fourth Cataract.'}],
 'next': 'Week 9: the Kushite pharaohs who ruled Egypt, the iron city of Meroe and its queens, and the Kingdom of Aksum.'}

TEACHER = {
 "standards": [
  "SS.6.W.3.18: Describe the rise and fall of the ancient east African kingdoms of Kush and Axum and Christianity's development in Ethiopia.",
  "SS.6.E.3.3: Describe traditional economies (Egypt, Greece, Rome, Kush) and elements of those economies that led to the rise of a merchant class and trading partners.",
  "SS.6.G.2.5: Interpret how geographic boundaries invite or limit interaction with other regions and cultures.",
  "SS.6.G.2.6: Explain the concept of cultural diffusion, and identify the influences of different ancient cultures on one another.",
  "SS.6.G.2.4: Explain how the geographical location of ancient civilizations contributed to the culture and politics of those societies.",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "C3 Framework D2.His.10.6-8: Detect possible limitations in the historical record based on evidence collected from different kinds of historical sources."],
 "materials": ["The interactive lesson", "A map of Africa", "Soil, water, dry grass or straw, molds (ice cube tray or paper cups), a bowl and spoon", "A ruler and some books", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 7 Reconnect questions."],
  [6, "Hook", "Show the map of Nubia and the cataracts. Explain Ta-Seti, the Land of the Bow."],
  [10, "A-Group and Qustul", "Present both sides of the Qustul debate. Ask the student what the object proves either way."],
  [12, "Kerma", "Show the Deffufa drawing. Discuss Kerma's trade, burials and how archaeology fills in for writing."],
  [12, "Kush strikes Egypt", "Tell the story of the Sobeknakht inscription. Discuss bias in royal records, then Egypt's conquest and Nubia's return to independence."],
  [8, "Napata", "Introduce Jebel Barkal and the rise of the new Kush. Preview the 25th Dynasty."],
  [6, "Assign", "Assign the mud-brick activity (start today; bricks need several days to dry), Think Deeper and the Exit Check."]],
 "key_questions": ["What can archaeology tell us when a people left no writing?", "Whose point of view does this source show?", "How did the balance of power between Kush and Egypt change, and why?", "Does borrowing ideas make a culture less important?"],
 "misconceptions": ["Thinking Nubia was just a part of Egypt.", "Believing Kerma was an Egyptian outpost (early researchers thought so; excavation proved otherwise).", "Assuming royal records tell the whole truth.", "Thinking that because Nubia lay south (upriver), it was \"below\" Egypt in importance."],
 "support": ["Provide a labeled map of Nubia to keep.", "Give a timeline card of the five main periods.", "Pair the Sobeknakht story with a simple cause-and-effect chart."],
 "challenge": ["Research the black granite statues of Kushite kings found by Charles Bonnet's team at Kerma (Dukki Gel) in 2003.", "Compare Kerma's royal burial mounds with the pyramids of Giza: what does each show about beliefs and power?"],
 "background": "<p>The A-Group flourished in Lower Nubia from about 3800 to 2900 BCE. The Qustul incense burner (Cemetery L, tomb 24, Oriental Institute, now ISAC Chicago) was interpreted by Bruce Williams (1980, 1986) as evidence that pharaonic kingship had Nubian roots; many scholars (for example, Wegner 1996) argue that Egyptian royal iconography is older and that A-Group rulers adopted it. Present both views; the debate continues. The Kingdom of Kerma (about 2500 to 1500 BCE; Classic Kerma about 1750 to 1580 BCE) was excavated by George Reisner (1913 to 1916) and Charles Bonnet (from the 1970s into the 2010s); the Western Deffufa's base measures about 52 by 27 m and its surviving height about 18 m. The Sobeknakht II inscription at Elkab (tomb 66/T10) was revealed during cleaning in 2003 and published by W. V. Davies (Egyptian Archaeology 23, 2003). Thutmose I campaigned in Kush around 1500 BCE; Kerma was destroyed under Thutmose III. The tomb of Huy (TT40) shows Nubian princes bringing tribute to Tutankhamun. The Napatan kingdom arose by the 9th to 8th century BCE at Jebel Barkal.</p>",
 "sources": ["Bonnet, C. (1992), Excavations at the Nubian royal town of Kerma: 1975-91, Antiquity 66.", "Davies, W. V. (2003), Sobeknakht of Elkab and the coming of Kush, Egyptian Archaeology 23.", "Williams, B. B. (1986), The A-Group Royal Cemetery at Qustul: Cemetery L, Oriental Institute Nubian Expedition III.", "Kendall, T. (1997), Kerma and the Kingdom of Kush, 2500-1500 BC, National Museum of African Art.", "Institute for the Study of Ancient Cultures, University of Chicago: The Qustul Incense Burner."]
}

PRINT = {
 "directions": "Use complete sentences and evidence.",
 "items": [
  {"q":"On separate paper, sketch the Nile from Aswan to Khartoum. Mark the six cataracts, Qustul, Kerma and Napata, and label Lower and Upper Nubia.","a":"Aswan at the 1st cataract; Qustul in Lower Nubia; Kerma near the 3rd; Napata near the 4th; Upper Nubia (Kush) south of the 2nd cataract.","lines":2},
  {"q":"Explain the two sides of the Qustul incense burner debate.","a":"Williams: Nubian kings used royal symbols as early as or earlier than Egypt; others: Egyptian symbols are older and Qustul's rulers borrowed them.","lines":3},
  {"q":"Give two reasons the Kingdom of Kerma became powerful.","a":"It controlled the Nile trade route and had valuable goods: gold, ivory, ebony, incense and cattle.","lines":2},
  {"q":"What did the Sobeknakht inscription reveal, and why was it surprising?","a":"Kush invaded deep into Egypt around 1575 to 1550 BCE; Egyptian royal records had kept quiet about it.","lines":2},
  {"q":"Describe how Egypt changed Nubia after conquering it, and how Kush became independent again.","a":"Egypt took gold and raised Nubian princes in Egypt; when Egypt weakened around 1070 BCE, Kush became independent.","lines":3},
  {"q":"Why was Jebel Barkal sacred?","a":"Kushites and Egyptians believed the god Amun lived inside the mountain.","lines":2}]
}
