from geo import NILE, BLUE_NILE

def roots():
    k = 11.0
    P = lambda lon, lat: (round((lon - 18) * k + 20, 1), round((33 - lat) * k + 34, 1))
    pts = lambda L: ' '.join('%s,%s' % P(*p) for p in L)
    mapw = 26 * k; W = int(mapw + 40 + 190); H = int(28 * k + 50)
    s = (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of the Nile Valley, Nubia and the eastern Sahara">'
         f'<text x="{W/2}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Kemet\'s African neighborhood</text>'
         f'<rect x="20" y="34" width="{mapw}" height="{28*k}" fill="#efe1bd"/>')
    s += f'<polygon points="{pts([(18,33),(44,33),(44,31.4),(34.2,31.2),(32,31.5),(30,31.6),(25,31.8),(20,32.3),(18,31.5)])}" fill="#bcd9ef"/>'
    west = [(32.6,29.9),(33.6,27.5),(35.4,24),(37.2,21),(38.6,18),(39.7,15.5),(41.5,13.3),(43,12.5)]
    east = [(44,12.6),(44,14.5),(41.2,17.5),(39.6,20.5),(38,24),(36.2,27),(34.9,29.5)]
    s += f'<polygon points="{pts(west + east)}" fill="#bcd9ef"/>'
    s += f'<text x="{P(23.5,26)[0]}" y="{P(23.5,26)[1]}" text-anchor="middle" font-size="13" fill="#8a6d1f" font-style="italic">Eastern Sahara</text><text x="{P(23.5,25)[0]}" y="{P(23.5,25)[1]}" text-anchor="middle" font-size="10" fill="#8a6d1f">green and wet about</text><text x="{P(23.5,24.1)[0]}" y="{P(23.5,24.1)[1]}" text-anchor="middle" font-size="10" fill="#8a6d1f">10,000 to 5,000 years ago</text>'
    s += f'<polyline points="{pts(NILE[2:])}" fill="none" stroke="#0047BA" stroke-width="3"/><polyline points="{pts(BLUE_NILE)}" fill="none" stroke="#0047BA" stroke-width="3"/>'
    marks = [(31.2, 29.85, 'Memphis'), (32.8, 25.1, 'Hierakonpolis'), (32.9, 24.1, 'Aswan'), (30.7, 22.5, 'Nabta Playa'), (32.0, 22.8, 'Lower Nubia'), (30.4, 19.7, 'Kerma'), (31.8, 18.5, 'Napata'), (33.75, 16.94, 'Meroe'), (32.5, 15.6, 'Khartoum'), (37.3, 12.0, 'Ethiopian Highlands')]
    lx = mapw + 34; last = -99
    for lon, lat, lab in marks:
        x, y = P(lon, lat); ly = max(y, last + 17); last = ly
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="#DB2F30" stroke="#fff"/><path d="M{x+4} {y} L{lx-4} {ly}" stroke="#8a8f99" stroke-width=".8"/><text x="{lx}" y="{ly+4}" font-size="11">{lab}</text>'
    s += (f'<text x="{P(28.6,27)[0]}" y="{P(28.6,27)[1]}" font-weight="bold" fill="#0A1F3D" font-size="11" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">KEMET</text>'
          f'<text x="{P(26.3,18.6)[0]}" y="{P(26.3,18.6)[1]}" font-weight="bold" fill="#5b4a1c" font-size="11" style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">NUBIA</text>'
          f'<text x="{P(19,32.3)[0]}" y="{P(19,32.3)[1]}" font-size="10" fill="#0A1F3D">Mediterranean Sea</text><text x="{P(37.6,21)[0]}" y="{P(37.6,21)[1]}" font-size="10" fill="#0A1F3D" transform="rotate(-55 {P(37.6,21)[0]} {P(37.6,21)[1]})">Red Sea</text></svg>')
    return s

ROOTS = roots()

def evidence():
    cats = [("Geography", "Egypt is in Africa. Its river and flood came from the south, and its first kings from Upper Egypt.", "#0047BA"),
            ("Archaeology", "Early Nile cultures shared pottery, cattle traditions and burial customs with Nubia and the Sahara.", "#0A1F3D"),
            ("Culture", "Divine kingship, headrests and cattle goddesses connect Kemet to other African societies.", "#C9A84C"),
            ("Language", "Egyptian belongs to the Afroasiatic family; many linguists place its origin in Africa.", "#DB2F30"),
            ("Written sources", "Egyptians named themselves after the Nile's black soil. A Greek visitor described them as dark-skinned.", "#0047BA"),
            ("Biology", "Early southern skeletons resemble Saharan and tropical Africans. Ancient DNA: mostly North African (also African).", "#0A1F3D")]
    s = ('<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Six kinds of evidence">'
         '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Six kinds of evidence that Kemet was African</text>')
    for i, (t, d, c) in enumerate(cats):
        x, y = 12 + (i % 3) * 182, 34 + (i // 3) * 132
        s += f'<rect x="{x}" y="{y}" width="172" height="122" rx="10" fill="{c}"/><text x="{x+86}" y="{y+24}" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">{t}</text>'
        words, line, lines = d.split(), '', []
        for w in words:
            if len(line + ' ' + w) > 27: lines.append(line); line = w
            else: line = (line + ' ' + w).strip()
        lines.append(line)
        for j, l in enumerate(lines):
            s += f'<text x="{x+86}" y="{y+46+j*15}" text-anchor="middle" fill="#fff">{l}</text>'
    return s + '</svg>'

TIMELINE = ('<svg viewBox="0 0 560 165" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="How Egypt was separated from Africa in European thinking and how scholars responded">'
  '<text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">How Egypt was pulled out of Africa, and put back</text>'
  '<line x1="30" y1="90" x2="530" y2="90" stroke="#0A1F3D" stroke-width="3"/>'
  + ''.join(f'<circle cx="{x}" cy="90" r="8" fill="{c}"/><text x="{x}" y="70" text-anchor="middle" font-weight="bold" font-size="12">{y}</text>'
            + ''.join(f'<text x="{x}" y="{114+j*14}" text-anchor="middle">{t}</text>' for j, t in enumerate(lines))
            for x, y, c, lines in [(60, "about 450 BCE", "#C9A84C", ["Herodotus calls", "Egyptians dark-", "skinned"]),
                                   (165, "1820s-1830s", "#DB2F30", ["Hegel's lectures:", "Egypt not part of", "\"the African spirit\""]),
                                   (275, "1800s-1900s", "#DB2F30", ["Race theories claim", "outsiders brought", "civilization"]),
                                   (385, "1954 and 1974", "#0047BA", ["Diop and Obenga", "argue Egypt was", "African"]),
                                   (490, "today", "#0047BA", ["Most scholars:", "Kemet grew from", "African roots"])]) + '</svg>')

LESSON = {'unit': 'Unit 2: The Nile Valley and Ancient Africa',
 'title': 'Kemet as an African Civilization',
 'subtitle': 'For two centuries, some writers tried to separate ancient Egypt from Africa. The evidence puts it right back where it belongs.',
 'objectives': ['Use six kinds of evidence to explain why Kemet was an African civilization.',
                'Explain how the ancient Egyptians described themselves and how a Greek visitor described them.',
                'Describe how European writers in the 1800s and 1900s separated Egypt from Africa, and why those ideas were wrong.',
                'Explain the work of Cheikh Anta Diop and Théophile Obenga.',
                'Evaluate evidence carefully, including what DNA can and cannot tell us.'],
 'vocab': [['civilization', 'A complex society with cities, government, writing, specialized jobs and shared beliefs.'],
           ['evidence', 'Information that helps prove or disprove a claim.'],
           ['divine kingship', 'The belief that a ruler is sacred or connected to the gods.'],
           ['Afroasiatic', 'A large language family that includes ancient Egyptian, Amazigh (Berber), Hausa, Somali, Amharic, Arabic and Hebrew.'],
           ['bias', 'A one-sided view that leads someone to favor or ignore certain evidence.'],
           ['racism', 'The false belief that some groups of people are better than others because of their race, and the unfair treatment that follows.'],
           ['Eurocentric', 'Viewing history and the world mainly from a European point of view.'],
           ['ancestry', 'The people a person is descended from.']],
 'reconnect': {'title': 'Week 6: the Nile and the rise of Kemet',
               'intro': "This week's evidence builds directly on last week's geography and history.",
               'items': [{'t': 'blanks',
                          'q': 'Complete the sentence.',
                          'sent': 'Upper Egypt is in the ___, and Egypt was unified by a ruler from Upper Egypt named ___.',
                          'blanks': [['south', 'southern', 'the south'], ['narmer', 'menes']],
                          'pts': 3,
                          'why': 'Upper Egypt is upstream (south). Narmer, from the south, is believed to have united Egypt around 3100 BCE.'},
                         {'t': 'text',
                          'q': 'What did the Egyptians call their country, and what does the name mean?',
                          'a': [{'all': [['kemet', 'kmt'], ['black']], 'none': ['not', 'red']}],
                          'show': 'Kemet, the Black Land',
                          'pts': 2,
                          'why': 'Kemet means the Black Land.'},
                         {'t': 'open',
                          'key': 'rc_ethiopia',
                          'q': 'Explain why the Nile flood depended on Ethiopia.',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Monsoon rains in the Ethiopian Highlands', 'Fed the Blue Nile, which caused most of the flood'],
                          'model': 'Heavy summer rains in the Ethiopian Highlands filled the Blue Nile, which brought most of the floodwater and silt north to Egypt.'},
                         {'t': 'open',
                          'key': 'rc_sahara',
                          'q': 'How did the drying of the Sahara help shape early Egypt?',
                          'min': 15,
                          'rows': 2,
                          'rubric': ['Herders and farmers moved from the Sahara toward the Nile', 'They brought traditions that helped form Nile cultures'],
                          'model': 'As the Sahara dried, herders and farmers moved toward the Nile Valley for water, bringing their cattle, pottery and customs, which helped form the early cultures '
                                   'of Upper Egypt.'}]},
 'hook': {'title': 'Who Gets to Tell the Story?',
          'visual': '<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="How Egypt was separated from Africa in European thinking '
                    'and how scholars responded"><text x="280" y="18" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">How Egypt was pulled out of Africa, and put '
                    'back</text><line x1="30" y1="90" x2="530" y2="90" stroke="#0A1F3D" stroke-width="3"/><circle cx="60" cy="90" r="8" fill="#C9A84C"/><text x="60" y="70" text-anchor="middle" '
                    'font-weight="bold" font-size="12">about 450 BCE</text><text x="60" y="114" text-anchor="middle">Herodotus calls</text><text x="60" y="128" text-anchor="middle">Egyptians '
                    'dark-</text><text x="60" y="142" text-anchor="middle">skinned</text><circle cx="165" cy="90" r="8" fill="#DB2F30"/><text x="165" y="70" text-anchor="middle" font-weight="bold" '
                    'font-size="12">1820s</text><text x="165" y="114" text-anchor="middle">Hegel claims Egypt</text><text x="165" y="128" text-anchor="middle">does not belong to</text><text x="165" '
                    'y="142" text-anchor="middle">"the African spirit"</text><circle cx="275" cy="90" r="8" fill="#DB2F30"/><text x="275" y="70" text-anchor="middle" font-weight="bold" '
                    'font-size="12">1800s-1900s</text><text x="275" y="114" text-anchor="middle">Race theories claim</text><text x="275" y="128" text-anchor="middle">outsiders brought</text><text '
                    'x="275" y="142" text-anchor="middle">civilization</text><circle cx="385" cy="90" r="8" fill="#0047BA"/><text x="385" y="70" text-anchor="middle" font-weight="bold" '
                    'font-size="12">1954 and 1974</text><text x="385" y="114" text-anchor="middle">Diop and Obenga</text><text x="385" y="128" text-anchor="middle">argue Egypt was</text><text '
                    'x="385" y="142" text-anchor="middle">African</text><circle cx="490" cy="90" r="8" fill="#0047BA"/><text x="490" y="70" text-anchor="middle" font-weight="bold" '
                    'font-size="12">today</text><text x="490" y="114" text-anchor="middle">Most scholars:</text><text x="490" y="128" text-anchor="middle">Kemet grew from</text><text x="490" y="142" '
                    'text-anchor="middle">African roots</text></svg>',
          'html': '<p>Open many older textbooks, movies or museum displays and you will see ancient Egypt shown almost as if it were part of Europe or the Middle East instead of Africa. In lectures '
                  'he gave in the 1820s, published after his death, the German philosopher Georg Hegel described Africa in racist terms, and a popular edition of those lectures says Egypt did not '
                  'belong to "the African spirit." In the 1800s and early 1900s, other writers invented race theories claiming that a lighter-skinned people from outside Africa must have brought '
                  'civilization to the Nile.</p><p>Those claims were not based on evidence. They came from <b>racism</b>: the false belief that Black Africans could not have built pyramids, invented '
                  "writing or run a great kingdom.</p><div class='callout'><b>Big idea:</b> Kemet was an African civilization, built by Africans along an African river. Historians prove this the "
                  'same way they prove anything: with evidence.</div>'},
 'learn': [{'title': "Kemet's African Roots",
            'visual': '<svg viewBox="0 0 516 358" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of the Nile Valley, Nubia and the eastern '
                      'Sahara"><text x="258.0" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Kemet\'s African neighborhood</text><rect x="20" y="34" width="286.0" '
                      'height="308.0" fill="#efe1bd"/><polygon points="20.0,34.0 306.0,34.0 306.0,51.6 198.2,53.8 174.0,50.5 152.0,49.4 97.0,47.2 42.0,41.7 20.0,50.5" fill="#bcd9ef"/><polygon '
                      'points="180.6,68.1 191.6,94.5 211.4,133.0 231.2,166.0 246.6,199.0 258.7,226.5 278.5,250.7 295.0,259.5 306.0,258.4 306.0,237.5 275.2,204.5 257.6,171.5 240.0,133.0 220.2,100.0 '
                      '205.9,72.5" fill="#bcd9ef"/><text x="80.5" y="111.0" text-anchor="middle" font-size="13" fill="#8a6d1f" font-style="italic">Eastern Sahara</text><text x="80.5" y="122.0" '
                      'text-anchor="middle" font-size="10" fill="#8a6d1f">green and wet about</text><text x="80.5" y="131.9" text-anchor="middle" font-size="10" fill="#8a6d1f">10,000 to 5,000 years '
                      'ago</text><polyline points="169.6,292.5 179.5,225.4 194.9,193.5 188.3,182.5 171.8,197.9 158.6,188.0 156.4,179.2 158.6,166.0 166.3,160.5 183.9,131.9 180.6,114.3 165.2,67.0 '
                      '163.0,52.7" fill="none" stroke="#0047BA" stroke-width="3"/><polyline points="232.3,265.0 207.0,248.5 179.5,225.4" fill="none" stroke="#0047BA" stroke-width="3"/><circle '
                      'cx="165.2" cy="68.6" r="4" fill="#DB2F30" stroke="#fff"/><path d="M169.2 68.6 L316.0 68.6" stroke="#8a8f99" stroke-width=".8"/><text x="320.0" y="72.6" '
                      'font-size="11">Memphis</text><circle cx="182.8" cy="120.9" r="4" fill="#DB2F30" stroke="#fff"/><path d="M186.8 120.9 L316.0 120.9" stroke="#8a8f99" stroke-width=".8"/><text '
                      'x="320.0" y="124.9" font-size="11">Hierakonpolis</text><circle cx="183.9" cy="131.9" r="4" fill="#DB2F30" stroke="#fff"/><path d="M187.9 131.9 L316.0 137.9" stroke="#8a8f99" '
                      'stroke-width=".8"/><text x="320.0" y="141.9" font-size="11">Aswan</text><circle cx="159.7" cy="149.5" r="4" fill="#DB2F30" stroke="#fff"/><path d="M163.7 149.5 L316.0 154.9" '
                      'stroke="#8a8f99" stroke-width=".8"/><text x="320.0" y="158.9" font-size="11">Nabta Playa</text><circle cx="169.6" cy="166.0" r="4" fill="#DB2F30" stroke="#fff"/><path '
                      'd="M173.6 166.0 L316.0 171.9" stroke="#8a8f99" stroke-width=".8"/><text x="320.0" y="175.9" font-size="11">Lower Nubia</text><circle cx="156.4" cy="181.4" r="4" fill="#DB2F30" '
                      'stroke="#fff"/><path d="M160.4 181.4 L316.0 188.9" stroke="#8a8f99" stroke-width=".8"/><text x="320.0" y="192.9" font-size="11">Kerma</text><circle cx="179.5" cy="225.4" r="4" '
                      'fill="#DB2F30" stroke="#fff"/><path d="M183.5 225.4 L316.0 225.4" stroke="#8a8f99" stroke-width=".8"/><text x="320.0" y="229.4" font-size="11">Khartoum</text><circle '
                      'cx="232.3" cy="265.0" r="4" fill="#DB2F30" stroke="#fff"/><path d="M236.3 265.0 L316.0 265.0" stroke="#8a8f99" stroke-width=".8"/><text x="320.0" y="269.0" '
                      'font-size="11">Ethiopian Highlands</text><text x="190.5" y="100.0" font-weight="bold" fill="#0A1F3D" font-size="11" '
                      'style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">KEMET</text><text x="187.2" y="188.0" font-weight="bold" fill="#5b4a1c" font-size="11" '
                      'style="paint-order:stroke;stroke:#efe1bd;stroke-width:4">NUBIA</text></svg>',
            'html': '<p><b>Geography.</b> Egypt is in Africa. Its water came from Central and East Africa, and its unification came from Upper Egypt in the south, next to '
                    'Nubia.</p><p><b>Archaeology.</b> The earliest farming cultures of Upper Egypt, the Badarian and Naqada, shared black-topped pottery, cattle herding and burial customs with '
                    'peoples of Lower Nubia and the eastern Sahara. Archaeologists such as Maria Gatto and Stuart Tyson Smith describe these cultures as closely related, with roots in the Saharan '
                    'wet period. Cattle were so important that the goddess Hathor was often shown as a cow or with cow horns.</p><p><b>Culture.</b> Kemet shared customs with other African societies: '
                    'a sacred, divine king who kept the world in balance; wooden headrests used as pillows (still used in parts of East Africa); and ceremonies honoring cattle and '
                    'ancestors.</p><p><b>Language.</b> Ancient Egyptian belongs to the Afroasiatic language family, along with Amazigh (Berber), Hausa, Somali and Amharic, as well as Arabic and '
                    'Hebrew. Most branches of this family are spoken in Africa, and many linguists, such as Christopher Ehret, place its origin in Africa.</p>',
            'checks': [{'t': 'open',
                        'key': 'pottery',
                        'q': 'Explain how pottery and cattle traditions help show that early Egypt grew from African roots.',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Early Upper Egyptian cultures shared pottery and cattle traditions with Nubia and the Sahara', 'Shared traditions suggest shared origins and contact'],
                        'model': 'The earliest cultures of Upper Egypt made the same kind of black-topped pottery and herded cattle like the peoples of Nubia and the eastern Sahara. Sharing these '
                                 'traditions shows they came from the same African roots and were connected.'},
                       {'t': 'blanks',
                        'q': 'Name two African languages in the same language family as ancient Egyptian.',
                        'sent': '___ and ___',
                        'blanks': [['amazigh', 'berber', 'hausa', 'somali', 'amharic', 'oromo', 'tigrinya', 'tamazight', 'tuareg', 'kabyle', 'afar', 'beja', 'tigre'],
                                   ['amazigh', 'berber', 'hausa', 'somali', 'amharic', 'oromo', 'tigrinya', 'tamazight', 'tuareg', 'kabyle', 'afar', 'beja', 'tigre']],
                        'distinct': True,
                        'show': 'For example: Hausa and Somali',
                        'pts': 2,
                        'why': 'Afroasiatic includes Amazigh (Berber), Hausa, Somali, Amharic and others, as well as Arabic and Hebrew.'},
                       {'t': 'open',
                        'key': 'headrest',
                        'q': 'Wooden headrests used as pillows are found in ancient Egyptian tombs and are still used in parts of East Africa today. What could this connection suggest, and why is '
                             'one object alone not enough to prove it?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Suggests a shared cultural tradition across Africa', 'Explains one object could be a coincidence; historians need many kinds of evidence'],
                        'model': 'It suggests that Egypt and East Africa shared a cultural tradition that lasted thousands of years. But one object alone could be a coincidence, so historians look '
                                 'for many kinds of evidence, like pottery, language and beliefs, that all point the same way.'},
                       {'t': 'open',
                        'key': 'mapcheck',
                        'q': "Using the map, explain why Hierakonpolis and Narmer are called southern, and name the region that was Kemet's closest neighbor upriver.",
                        'min': 15,
                        'rows': 2,
                        'rubric': ['Hierakonpolis lies far south in Upper Egypt, near Aswan, upstream', 'Nubia is the closest neighbor upriver (south)'],
                        'model': "Hierakonpolis is far up the Nile in Upper Egypt, close to Aswan, so it is in the south. Kemet's closest neighbor upriver was Nubia."}]},
           {'title': 'What the Ancient Sources Say',
            'html': '<p>The Egyptians called themselves <i>remetch en Kemet</i>, "the people of the Black Land." They also lived next to Nubia for thousands of years, trading, fighting, '
                    'intermarrying and sometimes ruling one another.</p><p>The Greek historian <b>Herodotus</b> visited Egypt around 450 BCE. In his <i>Histories</i> (Book 2), arguing that a people '
                    'called the Colchians were descended from Egyptian soldiers, he wrote that they were "dark-skinned and woolly-haired" like the Egyptians. He added that this alone proved little, '
                    'since other peoples looked that way too. Remember that Herodotus saw Egyptians about 2,000 years after the pyramids were built, so he describes the Egyptians of his own '
                    'time.</p><p>Most Egyptologists read <b>Kemet</b> as the dark, fertile Nile soil you studied in Week 6. Cheikh Anta Diop argued that the word also described the people. Either '
                    'way, the Egyptians named themselves after the African river land that made them, not after any land outside Africa.</p><p><b>Egyptian art</b> showed people in many shades. By '
                    'custom, artists often painted men a reddish brown and women a lighter yellow, so art colors were partly symbolic. Paintings also show Nubians, Libyans and people from Southwest '
                    'Asia with different features and clothing. The population itself varied: darker in the south near Nubia and lighter in parts of the north, as it still is along the Nile '
                    'today.</p>',
            'checks': [{'t': 'open',
                        'key': 'kemetname',
                        'q': 'Kemet means the Black Land. What did that name most likely refer to, and why is it still evidence of an African identity?',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Most likely the dark Nile soil (Diop argued it also described the people)',
                                   'The Egyptians named themselves after their African river land, not a land outside Africa'],
                        'model': 'Most Egyptologists think it referred to the dark, fertile soil left by the Nile flood, though Diop argued it also described the people. Either way, the Egyptians '
                                 'named themselves after the African river valley that made them, which shows they saw themselves as people of that land.'},
                       {'t': 'open',
                        'key': 'herodotus',
                        'q': 'Herodotus described Egyptians as dark-skinned. Is he a primary source? For which Egyptians? Give one strength and one weakness of his evidence.',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Yes, an eyewitness who visited Egypt',
                                   'Strength: he saw Egyptians in person',
                                   "Weakness: one outsider's view, made while arguing about another people, possibly with his own biases; he himself said appearance proved little",
                                   'Weakness: he saw Egyptians about 2,000 years after the pyramid builders'],
                        'model': 'Yes, he is a primary source because he visited Egypt and saw people himself. A strength is that he is an eyewitness. A weakness is that he was one foreign visitor '
                                 'making an argument about the Colchians, and he admitted appearance alone proves little, so historians compare him with other evidence. He also visited about 2,000 '
                                 'years after the pyramids were built, so he describes later Egyptians, not the pyramid builders.'},
                       {'t': 'open',
                        'key': 'artcolor',
                        'q': 'Egyptian artists usually painted men reddish brown and women light yellow. Why does this mean we should be careful using paint colors alone to decide what Egyptians '
                             'looked like?',
                        'min': 20,
                        'rows': 3,
                        'rubric': ['Colors followed artistic custom or symbolism, not exact skin tone', 'Need other evidence too'],
                        'model': 'The colors followed an artistic custom, so they were partly symbolic instead of exact skin tones. Real people varied, so we need other evidence, like skeletons and '
                                 'written descriptions, along with the art.'}]},
           {'title': 'Pulling Egypt Out of Africa',
            'html': '<p>Ancient Greek and Roman writers knew Egypt as a land of the Nile, and some placed the border between Asia and Libya (their name for Africa) at the river itself. But none of '
                    'them doubted that Egyptians were a people of the Nile Valley and neighbors of Nubia. The idea that Egypt was racially separate from Black Africa came much later, during the era '
                    'of European colonialism and the transatlantic slave trade.</p><ul><li><b>Hegel (lectures in the 1820s, published in the 1830s and 1840s)</b> described Africa in racist terms; '
                    'popular editions of his lectures divided Africa into parts and placed Egypt outside what they called "Africa proper."</li><li><b>The Hamitic theory</b> claimed that '
                    'lighter-skinned outsiders, not Black Africans, brought every achievement in Africa. It was used to justify colonial rule and is now completely rejected by '
                    'scholars.</li><li><b>The "dynastic race" theory</b> claimed a foreign master race invaded and founded Egypt\'s dynasties. Archaeology has shown Egyptian civilization grew '
                    'gradually inside the Nile Valley, so this theory has been abandoned.</li></ul><p>These ideas spread because they supported a racist picture of the world, not because the '
                    'evidence supported them.</p>',
            'checks': [{'t': 'open',
                        'key': 'whysplit',
                        'q': 'Why would writers during the era of colonialism and slavery want to separate Egypt from Africa? Explain the connection.',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Colonizers and enslavers claimed Africans could not build civilizations',
                                   "Egypt's achievements contradicted that claim, so they separated Egypt from Africa",
                                   'Connects bias to how history was written'],
                        'model': "Colonizers and enslavers claimed Africans had no history and could not build civilizations, which they used to excuse taking land and enslaving people. Egypt's "
                                 'pyramids and writing proved that claim wrong, so some writers separated Egypt from Africa instead of admitting it.'},
                       {'t': 'open',
                        'key': 'hamitic',
                        'q': 'In your own words, what was the Hamitic theory, and what does evidence show instead?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Claimed lighter-skinned outsiders brought achievements to Africa', 'Evidence shows African civilizations developed from African roots; the theory is rejected'],
                        'model': 'The Hamitic theory claimed that lighter-skinned people from outside Africa brought every great achievement to the continent. Evidence from archaeology, language and '
                                 'history shows that civilizations like Kemet grew from African roots, so scholars reject the theory.'}]},
           {'title': 'Putting Egypt Back: Diop, Obenga and the Evidence Today',
            'visual': '<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11" role="img" aria-label="Six kinds of evidence"><text x="280" y="18" '
                      'text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">Six kinds of evidence that Kemet was African</text><rect x="12" y="34" width="172" height="122" rx="10" '
                      'fill="#0047BA"/><text x="98" y="58" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Geography</text><text x="98" y="80" text-anchor="middle" '
                      'fill="#fff">Egypt is in Africa. Its</text><text x="98" y="95" text-anchor="middle" fill="#fff">river, its flood and its</text><text x="98" y="110" text-anchor="middle" '
                      'fill="#fff">first kings came from the</text><text x="98" y="125" text-anchor="middle" fill="#fff">south.</text><rect x="194" y="34" width="172" height="122" rx="10" '
                      'fill="#0A1F3D"/><text x="280" y="58" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Archaeology</text><text x="280" y="80" text-anchor="middle" '
                      'fill="#fff">Early Nile cultures shared</text><text x="280" y="95" text-anchor="middle" fill="#fff">pottery, cattle traditions</text><text x="280" y="110" text-anchor="middle" '
                      'fill="#fff">and burial customs with</text><text x="280" y="125" text-anchor="middle" fill="#fff">Nubia and the Sahara.</text><rect x="376" y="34" width="172" height="122" '
                      'rx="10" fill="#C9A84C"/><text x="462" y="58" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Culture</text><text x="462" y="80" text-anchor="middle" '
                      'fill="#fff">Divine kingship, headrests</text><text x="462" y="95" text-anchor="middle" fill="#fff">and cattle goddesses</text><text x="462" y="110" text-anchor="middle" '
                      'fill="#fff">connect Kemet to many</text><text x="462" y="125" text-anchor="middle" fill="#fff">African societies.</text><rect x="12" y="166" width="172" height="122" rx="10" '
                      'fill="#DB2F30"/><text x="98" y="190" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Language</text><text x="98" y="212" text-anchor="middle" '
                      'fill="#fff">Egyptian belongs to the</text><text x="98" y="227" text-anchor="middle" fill="#fff">Afroasiatic family; many</text><text x="98" y="242" text-anchor="middle" '
                      'fill="#fff">linguists place its origin</text><text x="98" y="257" text-anchor="middle" fill="#fff">in Africa.</text><rect x="194" y="166" width="172" height="122" rx="10" '
                      'fill="#0047BA"/><text x="280" y="190" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Written sources</text><text x="280" y="212" text-anchor="middle" '
                      'fill="#fff">Egyptians called themselves</text><text x="280" y="227" text-anchor="middle" fill="#fff">the people of Kemet. A</text><text x="280" y="242" text-anchor="middle" '
                      'fill="#fff">Greek visitor described</text><text x="280" y="257" text-anchor="middle" fill="#fff">them as dark-skinned.</text><rect x="376" y="166" width="172" height="122" '
                      'rx="10" fill="#0A1F3D"/><text x="462" y="190" text-anchor="middle" fill="#fff" font-weight="bold" font-size="13">Biology</text><text x="462" y="212" text-anchor="middle" '
                      'fill="#fff">Early southern skeletons</text><text x="462" y="227" text-anchor="middle" fill="#fff">resemble Saharan and</text><text x="462" y="242" text-anchor="middle" '
                      'fill="#fff">tropical Africans. Ancient</text><text x="462" y="257" text-anchor="middle" fill="#fff">DNA: mostly North African.</text></svg>',
            'html': '<p><b>Cheikh Anta Diop</b> (1923 to 1986), a Senegalese historian, anthropologist and physicist, argued in his 1954 book <i>Nations nègres et culture</i> that ancient Egypt was '
                    'a Black African civilization. At a 1974 UNESCO symposium in Cairo, he and the Congolese scholar <b>Théophile Obenga</b> presented evidence from language, culture and biology. '
                    "The symposium report praised their contributions as painstakingly researched. Not every expert agreed with all of Diop's conclusions, and some of his methods are debated, but "
                    "his work forced Egyptology to take Egypt's African roots seriously. The University of Dakar is now named Cheikh Anta Diop University.</p><p><b>Modern science</b> adds evidence. "
                    'Studies of skeletons from early southern Egypt, by scientists such as S. O. Y. Keita, find they resemble other Saharan and tropical African populations. In 2025, scientists '
                    'sequenced the first complete genome of an ancient Egyptian, a man who lived about 4,600 to 4,900 years ago. Most of his ancestry was North African, meaning ancestry from peoples '
                    'who had lived in North Africa for thousands of years (North Africa is Africa), and about one fifth came from the eastern Fertile Crescent, showing Egypt was also a crossroads. '
                    'The scientists cautioned that one person cannot represent a whole population. He was buried at Nuwayrat in Middle Egypt, not in the far south where the kingdom began, and '
                    "Egypt's heat destroys DNA, so ancient samples from the south are very rare.</p><p>Applying today's race labels to ancient people is tricky, because the Egyptians did not think "
                    'in modern categories. But the evidence is clear about where Kemet began. The people of the south, who united Egypt and founded its kingdom, were indigenous Africans whose '
                    'closest relatives were Saharan and tropical African peoples, people most of us today would call Black Africans. Over 3,000 years, Egypt also welcomed and absorbed Nubians, '
                    'Libyans and people from Southwest Asia, so its population varied from south to north. <b>The ancient Egyptians were Africans</b>, and Kemet was an African '
                    "civilization.</p><p>Next week you meet Kemet's southern neighbor and sometime ruler, Kush, whose kings ruled all of Egypt as the Twenty-fifth Dynasty.</p>",
            'checks': [{'t': 'open',
                        'key': 'diop',
                        'q': 'Who was Cheikh Anta Diop, and why is his work important even though not every expert agreed with every conclusion?',
                        'min': 30,
                        'rows': 3,
                        'rubric': ['Senegalese historian and scientist who argued Egypt was a Black African civilization',
                                   "His evidence (1954 book, 1974 UNESCO symposium) forced scholars to take Egypt's African roots seriously",
                                   'Recognizes that debate is normal in scholarship'],
                        'model': 'Cheikh Anta Diop was a Senegalese historian and scientist who argued that ancient Egypt was a Black African civilization. Even though some experts disagreed with '
                                 'parts of his work, his carefully researched evidence, shown at the 1974 UNESCO symposium, forced scholars to stop separating Egypt from Africa and to study its '
                                 'African roots.'},
                       {'t': 'open',
                        'key': 'dna',
                        'q': 'The 2025 genome came from one man. Explain why scientists said his DNA cannot represent all ancient Egyptians, and what this teaches about using evidence.',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['One person out of millions over 3,000 years and different regions',
                                   'Need many samples; avoid overgeneralizing from one piece of evidence',
                                   'Notes he was from Middle Egypt, not the south where the kingdom began, and that southern DNA rarely survives'],
                        'model': 'He was one person from one place and one time, but millions of people lived in Egypt over 3,000 years, and people in the south and north differed. Scientists need '
                                 'many samples before making conclusions, so we should not overgeneralize from a single piece of evidence. He also came from Middle Egypt, not the far south where the '
                                 'kingdom began, and DNA from the hot south rarely survives.'},
                       {'t': 'open',
                        'key': 'sixkinds',
                        'q': 'Look at the six kinds of evidence. Which kind do you find most convincing that Kemet was an African civilization, and why?',
                        'min': 25,
                        'rows': 3,
                        'rubric': ['Chooses a kind of evidence', 'Explains why it is convincing with specifics'],
                        'model': 'Archaeology is most convincing to me, because pottery, cattle bones and burials are physical evidence that shows the early Nile cultures were closely related to '
                                 "Nubia and the Sahara, without depending on one writer's opinion."}]}],
 'handson': {'title': 'Build an Evidence Wall',
             'intro': 'Historians build arguments the way builders build walls: one piece of evidence at a time. Build yours on a wall, a door or a large poster.',
             'materials': ['12 or more sticky notes or index cards', 'Tape', 'Markers in two colors', 'A wall, door or poster board', 'A map of Africa'],
             'steps': ['Write the claim at the top: Kemet was an African civilization.',
                       'Make six column headers: Geography, Archaeology, Culture, Language, Written sources, Biology.',
                       'Tape the map of Africa beside your wall and mark the Nile, Nubia, the Sahara and the Ethiopian Highlands for your Geography cards.',
                       'Write each piece of evidence from the lesson on its own card and place it in the right column. Aim for at least two cards per column.',
                       'In a second color, add a card for any evidence that is limited or debated (for example, one genome, or art colors that were symbolic), and place it beside the evidence it '
                       'limits.',
                       'Present your wall to a family member in 3 minutes. Ask them which card convinced them most.'],
             'record': [{'t': 'open',
                         'key': 'wall',
                         'q': 'Type the cards from your evidence wall, column by column, including your limit cards.',
                         'min': 80,
                         'rows': 10,
                         'rubric': ['Six columns, at least two cards each', 'Accurate evidence from the lesson', 'At least two limit cards that explain weaknesses'],
                         'model': "Geography: Egypt is in Africa; unification came from the south. Archaeology: Badarian and Naqada pottery like Nubia's; cattle herding. Culture: divine kingship; "
                                  "headrests; Hathor as a cow. Language: Egyptian is Afroasiatic; related to Hausa and Somali. Written sources: Egyptians named themselves after Kemet, the Nile's "
                                  'black soil; Herodotus said dark-skinned (but 2,000 years after the pyramids). Biology: early southern skeletons resemble Saharan and tropical Africans; 2025 genome '
                                  'mostly North African. Limit cards: Herodotus was one outsider; art colors were symbolic; the genome is only one person.'},
                        {'t': 'open',
                         'key': 'walltalk',
                         'q': 'Which card did your family member find most convincing, and what question did they ask? How did you answer?',
                         'min': 25,
                         'rows': 3,
                         'rubric': ["Reports the listener's choice", 'Reports a question and an evidence-based answer'],
                         'model': 'My dad thought the pottery and cattle card was most convincing. He asked why movies show Egyptians as European. I explained that writers in the 1800s separated '
                                  'Egypt from Africa because of racism, and that the evidence shows Egyptians were Africans.'}]},
 'think': {'intro': 'Write an evidence-based argument. Your teacher scores these.',
           'items': [{'t': 'open',
                      'key': 'argument',
                      'q': 'Write a paragraph arguing that ancient Kemet was an African civilization. Use at least four pieces of evidence from at least three different kinds (geography, '
                           'archaeology, culture, language, written sources, biology). Then explain why some writers in the past claimed otherwise and why they were wrong.',
                      'min': 150,
                      'rows': 14,
                      'rubric': ['Clear claim',
                                 'Four or more accurate pieces of evidence from three or more kinds',
                                 'Explains the history of the opposing claims (Hegel, Hamitic theory, dynastic race theory)',
                                 'Explains why those claims were wrong (racism, no evidence)',
                                 'Organized, with a conclusion'],
                      'model': "Ancient Kemet was an African civilization, built by Africans along an African river. Geographically, Egypt is in Africa: the Nile's water came from Central and East "
                               'Africa, and the kingdom was united by Narmer, a ruler from the south. Archaeologists have found that the earliest Upper Egyptian cultures, the Badarian and Naqada, '
                               'made the same black-topped pottery and herded cattle like their neighbors in Nubia and the Sahara. Culturally, Kemet shared divine kingship and wooden headrests with '
                               'many African societies. Its language belonged to the Afroasiatic family, along with Hausa and Somali. The Egyptians named themselves after Kemet, the black soil of '
                               'their African river valley, and Herodotus, though writing much later, described them as dark-skinned. In the 1800s, writers like Hegel and the creators of the Hamitic '
                               'theory claimed that civilization must have come from outside Africa. They had no evidence; they were defending a racist view of the world that was used to justify '
                               'colonialism and slavery. When historians follow the evidence instead of prejudice, Kemet stands where it always stood: in Africa.'},
                     {'t': 'open',
                      'key': 'media',
                      'q': "A movie about ancient Egypt casts only actors of European descent as the pharaoh and his family. Using this week's evidence, write a short, respectful letter to the "
                           'filmmakers explaining what is inaccurate and what you would suggest.',
                      'min': 70,
                      'rows': 7,
                      'rubric': ['Respectful tone and letter format',
                                 'Explains with evidence why the casting misrepresents Egyptians',
                                 'Offers a constructive suggestion',
                                 "Acknowledges Egypt's variety without erasing its African identity"],
                      'model': 'Dear Filmmakers, I enjoyed seeing ancient Egypt on screen, but your casting gives viewers a false picture. The ancient Egyptians were Africans: their kingdom was '
                               'united from the south, their early cultures were closely related to Nubia and the Sahara, and a Greek visitor described them as dark-skinned. Showing only actors of '
                               'European descent repeats an idea from the 1800s that separated Egypt from Africa. I suggest casting actors who reflect the people of the Nile Valley and Nubia, and '
                               'working with Egyptian and other African historians. Thank you for considering this. Sincerely, a Grade 6 historian'}]},
 'exit': [{'t': 'open',
           'key': 'exit_claim',
           'q': 'Give two different kinds of evidence that Kemet was an African civilization.',
           'min': 15,
           'rows': 2,
           'rubric': ['Two accurate pieces of evidence from two different kinds'],
           'model': 'Archaeology: early Upper Egyptian pottery and cattle traditions match Nubia and the Sahara. Language: Egyptian is in the Afroasiatic family with Hausa and Somali.'},
          {'t': 'text',
           'q': 'Which Senegalese scholar argued that ancient Egypt was a Black African civilization and presented evidence at the 1974 UNESCO symposium?',
           'a': ['cheikh anta diop', 'diop', 'anta diop'],
           'show': 'Cheikh Anta Diop',
           'pts': 2,
           'why': 'Cheikh Anta Diop, with Théophile Obenga.'},
          {'t': 'open',
           'key': 'exit_genome',
           'q': 'What did the 2025 genome show, and what is one reason it cannot settle the question alone?',
           'min': 15,
           'rows': 2,
           'rubric': ['Mostly North African ancestry, about one fifth Fertile Crescent', 'A real limit (one person; Middle Egypt not the south; DNA rarely survives)'],
           'model': 'It showed one man with mostly North African ancestry and about one fifth from the Fertile Crescent. It cannot settle the question because he is only one person from Middle '
                    'Egypt, not the south where the kingdom began.'},
          {'t': 'open',
           'key': 'exit_dynastic',
           'q': 'Explain how the "dynastic race" theory was disproved.',
           'min': 12,
           'rows': 2,
           'rubric': ['It claimed a foreign master race founded Egypt', 'Archaeology shows Egyptian civilization grew gradually inside the Nile Valley'],
           'model': "It claimed a foreign master race invaded and founded Egypt's kingdom, but archaeology shows Egyptian civilization grew gradually from earlier Nile Valley cultures like the "
                    'Badarian and Naqada.'},
          {'t': 'open',
           'key': 'exit_hero',
           'q': 'Herodotus visited Egypt about 2,000 years after the Great Pyramid was built. Why is that a limit of his evidence?',
           'min': 10,
           'rows': 2,
           'rubric': ['He describes Egyptians of his own time, not the pyramid builders; populations and customs change over 2,000 years'],
           'model': 'He could only describe the Egyptians of his own time, and a lot can change in 2,000 years, so his account is weaker evidence about the people who built the pyramids.'}],
 'next': "Week 8: Nubia and the Kingdom of Kush, Kemet's powerful neighbor to the south, with its own kings, queens, pyramids and gold."}

TEACHER = {
 "standards": [
  "SS.6.W.2.5: Summarize important achievements of Egyptian civilization.",
  "SS.6.W.1.4: Describe the methods of historical inquiry and how history relates to the other social sciences.",
  "SS.6.W.1.5: Describe the roles of historians and recognize varying historical interpretations (historiography).",
  "SS.6.W.1.3: Interpret primary and secondary sources.",
  "SS.6.G.2.4: Explain how the geographical location of ancient civilizations contributed to the culture and politics of those societies.",
  "C3 Framework D2.His.6.6-8: Analyze how people's perspectives influenced what information is available in the historical sources they created."],
 "materials": ["The interactive lesson", "12 or more sticky notes or index cards, tape and markers in two colors", "A wall, door or poster board", "A map of Africa", "Printable practice page"],
 "flow": [
  [6, "Reconnect", "Run the Week 6 Reconnect questions."],
  [8, "Hook", "Show the timeline. Ask: why would anyone want to separate Egypt from Africa?"],
  [12, "African roots", "Use the map. Discuss archaeology, culture and language as evidence."],
  [10, "Ancient sources", "Read the Herodotus passage and discuss art conventions as evidence with limits."],
  [10, "Pulling Egypt out", "Explain Hegel, the Hamitic theory and the dynastic race theory, and the racism behind them."],
  [10, "Putting Egypt back", "Introduce Diop and Obenga, modern skeletal and DNA evidence, and its limits."],
  [4, "Assign", "Assign the Evidence Wall, Think Deeper and the Exit Check."]],
 "key_questions": ["What kind of evidence is this, and how strong is it?", "Whose perspective shaped this source?", "Why did false ideas spread even without evidence?", "What can one genome tell us, and what can't it?"],
 "misconceptions": ["Picturing ancient Egypt as part of Europe or the Middle East rather than Africa.", "Believing outsiders brought civilization to Africa.", "Treating Egyptian paint colors as exact skin tones.", "Overgeneralizing from a single DNA sample, in either direction.", "Assuming all ancient Egyptians looked exactly alike."],
 "support": ["Provide the six evidence categories as a printed organizer.", "Give sentence frames for the argument: One piece of evidence is... This shows... Some writers claimed... However...", "Let the student talk through the Evidence Wall before writing."],
 "challenge": ["Read a short excerpt from Diop's The African Origin of Civilization (1974 English translation) and summarize one argument.", "Research Amenemhat I, founder of the Twelfth Dynasty, described in the Prophecy of Neferti as the son of a woman of Ta-Seti, the southernmost region bordering Nubia, and report what the evidence shows."],
 "background": "<p>This lesson teaches Kemet as an African civilization using evidence. It presents the mainstream archaeological view that Egyptian civilization developed indigenously in the Nile Valley with strong Saharan and Nubian connections (Gatto; Smith 2018; Wengrow), the historiography of racist separation (Hegel's Lectures on the Philosophy of World History, as edited by Gans in 1837 and Karl Hegel in 1840; Bernasconi 2024 shows Hegel's own lectures stressed Egypt's African element in racist terms; the Hamitic hypothesis; Petrie's dynastic race theory), Diop's Nations nègres et culture (1954) and the 1974 UNESCO Cairo symposium (where the rapporteur called Diop's and Obenga's contributions painstakingly researched, while many participants disagreed with parts of their conclusions), Keita's craniometric work describing predynastic southern Egyptians as a Saharo-tropical African variant, and the 2025 Nature genome from Nuwayrat (Morez Jacobs et al.; radiocarbon dated about 2855 to 2570 BCE; about 80 percent North African Neolithic ancestry and about 20 percent eastern Fertile Crescent ancestry; the authors caution that one individual may not represent the population). Herodotus 2.104 (Godley translation) describes the Colchians as \"dark-skinned and woolly-haired\" in comparing them with Egyptians. Egyptian art conventions (reddish-brown men, yellow women) are partly symbolic. The lesson avoids imposing modern racial categories while stating clearly that the ancient Egyptians were Africans.</p>",
 "sources": ["UNESCO General History of Africa, Volume II, including the report of the 1974 Cairo symposium.", "Diop, C. A. (1974), The African Origin of Civilization: Myth or Reality.", "Morez Jacobs, A. et al. (2025), Whole-genome ancestry of an Old Kingdom Egyptian, Nature 644.", "Herodotus, Histories 2.104 (trans. A. D. Godley, Loeb Classical Library).", "Smith, S. T. (2018), Ethnicity: constructions of self and other in ancient Egypt, Journal of Egyptian History.", "Wengrow, D. et al. (2014), Cultural convergence in the Neolithic of the Nile Valley: a prehistoric perspective on Egypt's place in Africa, Antiquity 88.", "Bernasconi, R. (2024), Hegel and Egypt's African Element, Hegel Bulletin.", "Keita, S. O. Y. (1990, 1993), studies of early Nile Valley crania."]
}

PRINT = {
 "directions": "Use complete sentences and specific evidence.",
 "items": [
  {"q":"Name the six kinds of evidence from this lesson and give one example of two of them.","a":"Geography, archaeology, culture, language, written sources, biology. For example: archaeology, black-topped pottery like Nubia's; language, Egyptian is Afroasiatic with Hausa.","lines":3},
  {"q":"What did the ancient Egyptians call themselves?","a":"remetch en Kemet, the people of the Black Land","lines":1},
  {"q":"Explain what Hegel and the Hamitic theory claimed, and why historians reject those claims.","a":"They claimed Egypt was not truly African and that outsiders brought civilization; historians reject them because they were based on racism, not evidence.","lines":3},
  {"q":"Who was Cheikh Anta Diop, and what happened at the 1974 UNESCO symposium?","a":"A Senegalese historian and scientist who argued Egypt was a Black African civilization; he and Théophile Obenga presented evidence in Cairo, and their work was praised as painstakingly researched.","lines":3},
  {"q":"Give one strength and one limit of DNA evidence about ancient Egyptians.","a":"Strength: it shows real ancestry (the 2025 genome was mostly North African). Limit: one person cannot represent millions over 3,000 years.","lines":2},
  {"q":"Write a one-sentence claim about Kemet that you can support with evidence.","a":"For example: Kemet was an African civilization whose earliest cultures grew from the traditions of Nubia and the Sahara.","lines":2}]
}
