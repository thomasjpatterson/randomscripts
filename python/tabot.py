import requests
from bs4 import BeautifulSoup

# Define a dictionary of threat actor names and their aliases
threat_actors = {
  'APT1': ['Comment Crew'],
  'APT2': ['APT2'],
  'APT3': ['Gothic Panda'],
  'APT4': ['APT4'],
  'APT5': ['APT5'],
  'APT6': ['APT6'],
  'APT7': ['Unit 61398'],
  'APT8': ['APT8'],
  'APT9': ['APT9'],
  'APT10': ['MenuPass'],
  'APT11': ['APT11'],
  'APT12': ['GuruSpider'],
  'APT13': ['BraceSound'],
  'APT14': ['APT14'],
  'APT15': ['Ke3chang'],
  'APT16': ['APT16'],
  'APT17': ['Deadeye Jackal'],
  'APT18': ['Thrip'],
  'APT19': ['Codoso'],
  'APT20': ['Ke4'],
  'APT21': ['APT21'],
  'APT22': ['APT22'],
  'APT23': ['Elfin'],
  'APT24': ['APT24'],
  'APT25': ['Naikon'],
  'APT26': ['BlackOasis'],
  'APT27': ['Emissary Panda'],
  'APT28': ['Fancy Bear'],
  'APT29': ['Cozy Bear'],
  'APT30': ['Zirconium'],
  'APT31': ['Zirconium'],
  'APT32': ['OceanLotus'],
  'APT33': ['Elfin'],
  'APT34': ['OilRig'],
  'APT35': ['Newscaster'],
  'APT36': ['APT36'],
  'APT37': ['Reaper'],
  'APT38': ['APT38'],
  'APT39': ['Chafer'],
  'APT40': ['APT40'],
  'APT41': ['APT41'],
  'APT42': ['Whitefly'],
  'APT43': ['APT43'],
  'APT44': ['APT44'],
  'APT45': ['APT45'],
  'APT46': ['APT46'],
  'APT47': ['Mustang Panda'],
  'APT48': ['Temp.Periscope'],
  'APT49': ['APT49'],
  'APT50': ['APT50'],
  'APT51': ['APT51'],
  'DarkHotel': ['DarkHotel'],
  'DarkHydrus': ['DarkHydrus'],
  'DarkRat': ['DarkRat'],
  'DarkUniverse': ['DarkUniverse'],
  'DarkVishnya': ['DarkVishnya'],
  'DarkWinds': ['DarkWinds'],
  'DarkZone': ['DarkZone'],
  'Deep Panda': ['Deep Panda'],
  'Dragonfly': ['Dragonfly'],
  'Elderwood': ['Elderwood'],
  'Equation Group': ['Equation Group'],
  'FIN4': ['FIN4'],
  'FIN5': ['FIN5'],
  'FIN6': ['FIN6'],
  'FIN7': ['FIN7'],
  'FIN8': ['FIN8'],
  'FIN9': ['FIN9'],
  'Gamaredon Group': ['Gamaredon Group'],
  'GCMAN': ['GCMAN'],
  'Gorgon Group': ['Gorgon Group'],
  'Honeybee': ['Honeybee'],
  'Icefog': ['Icefog'],
  'Inception Framework': ['Inception Framework'],
  'Iron Group': ['Iron Group'],
  'Kimsuky': ['Kimsuky'],
  'Lazarus': ['Lazarus']
}

# Define the URLs for the news resources
# Loop through the URLs and extract relevant web page URLs
# Define the URLs of the news resources

urls = [
  'https://www.fireeye.com/blog/threat-research.html',
  'https://www.kaspersky.com/blog/tag/apt',
  'https://www.ncsc.gov.uk/news/reports',
  'https://thehackernews.com/search/label/apt',
  'https://www.recordedfuture.com/apt-group-threat-intelligence/',
  'https://www.anomali.com/blog/threat-research',
  'https://www.mandiant.com/resources/blog',
  'https://www.symantec.com/blogs/threat-intelligence',
  'https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks',
  'https://www.welivesecurity.com/category/apt/',
  'https://www.zdnet.com/topic/security/',
  'https://www.crowdstrike.com/blog/category/threat-intel-research/',
  'https://securelist.com/all/',
  'https://unit42.paloaltonetworks.com/',
  'https://www.proofpoint.com/us/threat-insight',
  'https://www.secureworks.com/research/threat-profiles',
  'https://www.sophos.com/en-us/threat-center/threat-analyses.aspx',
  'https://www.talosintelligence.com/vulnerability_reports',
  'https://www.symantec.com/blogs',
  'https://research.checkpoint.com/',
  'https://www.recordedfuture.com/blog/',
  'https://threatpost.com/'
]

webpage_urls = []
for url in urls:
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        for actor in threat_actors:
            if actor in link.text or any(alias in link.text for alias in threat_actors[actor]):
                webpage_urls.append(href)

# Print the extracted webpage URLs
for url in webpage_urls:
    print(url)