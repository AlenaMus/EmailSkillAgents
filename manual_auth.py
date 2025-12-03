#!/usr/bin/env python3
"""
Manual OAuth Authentication Helper
Provides the URL for manual browser authorization
"""

import sys
sys.path.insert(0, '.')

from gmailagent.auth import GmailAuthenticator
from google_auth_oauthlib.flow import InstalledAppFlow

print("=" * 70)
print("GmailAgent - Manual Authentication")
print("=" * 70)
print()

try:
    auth = GmailAuthenticator()

    # Check if already authenticated
    if auth.is_authenticated():
        print("✓ Already authenticated!")
        print()
        print("You can now export emails:")
        print('  python -m gmailagent.cli export --tag "aiDevelopmentCourse"')
        sys.exit(0)

    print("Starting manual authentication...")
    print()

    # Start the OAuth flow with manual URL display
    flow = InstalledAppFlow.from_client_secrets_file(
        str(auth.credentials_path),
        scopes=['https://www.googleapis.com/auth/gmail.readonly']
    )

    # Run local server without opening browser
    print("=" * 70)
    print("COPY THIS URL AND OPEN IT IN YOUR BROWSER:")
    print("=" * 70)

    # This will print the URL and wait for callback
    creds = flow.run_local_server(
        port=0,
        open_browser=False,
        authorization_prompt_message='\nWaiting for authorization...\nAfter authorizing in browser, come back here.\n'
    )

    # Save the credentials
    import pickle
    with open(auth.token_path, 'wb') as token:
        pickle.dump(creds, token)

    print()
    print("=" * 70)
    print("✓ Authentication successful!")
    print("=" * 70)
    print()
    print("You can now export emails:")
    print('  python -m gmailagent.cli export --tag "aiDevelopmentCourse"')

except Exception as e:
    print()
    print(f"Error: {e}")
    print()
    import traceback
    traceback.print_exc()
    sys.exit(1)
