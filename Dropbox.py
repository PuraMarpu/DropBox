import dropbox

class Transfer:
    def __init__(self, accessToken):
        self.Token = accessToken
    
    def UploadFile( self, src, dst ):
        dropB = dropbox.Dropbox(self.Token)

        with open(src, 'rb') as file:
            dropB.files_upload(file.read(), dst)


def main():
    Accestoken = 'sl.BAYuWbxmKB8JrlYxb7Y7VlazZyUqnT0LtuePt3jYmAdgRao9SBYIWmVwrTsMNh4NMxNkS4xbEl58W7b15DOhHTpyrwMPsL8LwAzUOSM8VwVrLEs-7Zebk48Yub9x3zlHcBi07uxFHDiQ'
    
    FileObj = Transfer( Accestoken )
    usrInpt = input(' Put the source:  ')
    usrInpt2 = input()

    FileObj.UploadFile(usrInpt, usrInpt2)

    print('Done')

main()