from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials


def upload_basic():
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    #creds, _ = google.auth.default()
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': 'first-uploaded-file.jpeg'}
        media = MediaFileUpload('download.jpg',
                                mimetype='image/jpeg')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id, webViewLink, version, permissions, owners, parents').execute()
        print(F'File ID: {file.get("id")}')
        print(F'File webViewLink: {file.get("webViewLink")}')
        print(F'File version: {file.get("version")}')
        print(F'File permissions: {file.get("permissions")}')
        print(F'File owners: {file.get("owners")}')
        print(F'File parents: {file.get("parents")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


if __name__ == '__main__':
    upload_basic()