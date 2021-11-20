def makeAlbum(artistName, albumTitle, songNumber=None):
    """Return a dictionary of album info"""
    albumInfo = {'artist':  artistName, 'album':  albumTitle}
    if songNumber:
        albumInfo['songNumber'] = songNumber
    return albumInfo

while True:
    print("\nPlease recommend me music:")
    print("(enter 'q' at any time to quit)")

    sName = input("Artist name: ")
    if sName == 'q':
        break
    aName = input("Album name: ")
    if aName == 'q':
        break

    album = makeAlbum(sName, aName)
    print(f"\n{album}")
#album = makeAlbum('rush', 'moving pictures', '7')
#print(album)
#album = makeAlbum('yes', 'fragile')
#print(album)