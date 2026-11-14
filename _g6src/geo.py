"""Simple, roughly accurate SVG maps (equirectangular) for KCE Grade 6 social studies."""

AFRICA = [(-5.8,35.8),(3,36.8),(10.2,37),(11,33.5),(13,32.9),(15.5,31.5),(20,30.5),(20,32.2),(25,31.7),(29.9,31.2),(32.3,31.3),
 (32.5,29.9),(35,24),(37.2,19.6),(39.5,15.5),(43.3,11.6),(51.2,11.8),(49,7),(45.3,2),(41,-1.5),(39.7,-4),(39.3,-6.8),(40.5,-10.5),
 (40.7,-15),(35.4,-23.9),(32.6,-26),(31,-29.9),(27.9,-33),(25.6,-34),(20,-34.8),(18.4,-34),(17,-29.7),(14.5,-22.9),(11.8,-17),
 (13.2,-8.8),(12.3,-6),(9.3,-0.7),(9.5,4),(6.5,4.3),(3.4,6.4),(-0.2,5.5),(-4,5.3),(-7.5,4.4),(-10.8,6.3),(-13.2,8.5),(-16.8,13),
 (-17.4,14.7),(-16,19),(-17,21),(-13,27.5),(-9.6,30.4),(-6.8,34)]
MADAGASCAR = [(44.3,-25),(47,-25),(49.5,-15.5),(50.4,-15.4),(49.3,-12),(48,-13.5),(44,-17),(43.3,-22)]
NILE = [(33,-1),(32.5,4),(31.6,9.5),(32.5,15.6),(33.9,18.5),(31.3,21.5),(32.9,24.1),(32.6,25.7),(31.2,30),(31,31.3)]
BLUE_NILE = [(37.3,12),(35,13.5),(32.5,15.6)]
NIGER = [(-10.5,9.5),(-8,12.6),(-4,14.5),(-3,16.8),(0,16.3),(3.5,11.8),(6.5,8),(6.5,4.6)]


def africa_map(markers=(), title='', rivers=True, w=420):
    k, x0, y0 = 5.6, -20, 38
    P = lambda lon, lat: (round((lon - x0) * k + 10, 1), round((y0 - lat) * k + 34, 1))
    pts = lambda L: ' '.join('%s,%s' % P(*p) for p in L)
    h = int((y0 + 36) * k + 44)
    s = f'<svg viewBox="0 0 {int(73*k+20)} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of Africa{": " + title if title else ""}">'
    if title: s += f'<text x="{int(73*k/2+10)}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">{title}</text>'
    s += f'<rect x="0" y="28" width="{int(73*k+20)}" height="{h-28}" fill="#eaf4fb"/>'
    s += f'<polygon points="{pts(AFRICA)}" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1.5"/><polygon points="{pts(MADAGASCAR)}" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1.5"/>'
    ex, ey = P(-20, 0); ex2, _ = P(53, 0)
    s += f'<line x1="{ex}" y1="{ey}" x2="{ex2}" y2="{ey}" stroke="#DB2F30" stroke-dasharray="5 4"/><text x="{ex2-4}" y="{ey-4}" text-anchor="end" fill="#DB2F30" font-size="10">Equator</text>'
    if rivers:
        s += f'<polyline points="{pts(NILE)}" fill="none" stroke="#0047BA" stroke-width="2.5"/><polyline points="{pts(BLUE_NILE)}" fill="none" stroke="#0047BA" stroke-width="2"/>'
        s += f'<polyline points="{pts(NIGER)}" fill="none" stroke="#0047BA" stroke-width="2"/>'
        nx, ny = P(33.5, 20); s += f'<text x="{nx+4}" y="{ny}" fill="#0047BA" font-size="11" font-style="italic">Nile</text>'
        gx, gy = P(-1, 13.5); s += f'<text x="{gx}" y="{gy}" fill="#0047BA" font-size="11" font-style="italic">Niger</text>'
    for m in markers:
        lon, lat, label = m[0], m[1], m[2]
        dx = m[3] if len(m) > 3 else 6; dy = m[4] if len(m) > 4 else 4
        x, y = P(lon, lat)
        anchor = 'end' if dx < 0 else 'start'
        s += f'<circle cx="{x}" cy="{y}" r="4.5" fill="#C9A84C" stroke="#0A1F3D" stroke-width="1.5"/><text x="{x+dx}" y="{y+dy}" text-anchor="{anchor}" font-size="11" font-weight="bold" fill="#0A1F3D">{label}</text>'
    return s + '</svg>'


FLORIDA = [(-87.6,31),(-85,31),(-84.9,30.7),(-82.2,30.6),(-81.4,30.7),(-81.2,29.5),(-80.6,28.4),(-80.1,26.9),(-80.1,25.8),(-80.4,25.2),
 (-81.1,25.1),(-81.8,26.1),(-82.2,26.7),(-82.8,27.9),(-82.7,28.9),(-83.7,29.9),(-84.4,29.9),(-85.4,29.7),(-86.5,30.4),(-87.6,30.3)]


def florida_map(regions=(), title=''):
    k, x0, y0 = 42, -88, 31.4
    P = lambda lon, lat: (round((lon - x0) * k + 10, 1), round((y0 - lat) * k + 30, 1))
    s = f'<svg viewBox="0 0 {int(8.4*k+20)} {int(6.7*k+40)}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="12" role="img" aria-label="Map of Florida{": " + title if title else ""}">'
    if title: s += f'<text x="{int(8.4*k/2+10)}" y="20" text-anchor="middle" font-weight="bold" fill="#0A1F3D" font-size="15">{title}</text>'
    s += f'<rect x="0" y="26" width="{int(8.4*k+20)}" height="{int(6.7*k+14)}" fill="#eaf4fb"/>'
    s += '<polygon points="%s" fill="#f3e7c9" stroke="#8a6d1f" stroke-width="1.5"/>' % ' '.join('%s,%s' % P(*p) for p in FLORIDA)
    for lon, lat, label in regions:
        x, y = P(lon, lat)
        s += f'<circle cx="{x}" cy="{y}" r="5" fill="#0047BA" opacity=".25"/><text x="{x}" y="{y+4}" text-anchor="middle" font-size="12" font-weight="bold" fill="#0A1F3D">{label}</text>'
    return s + '</svg>'
