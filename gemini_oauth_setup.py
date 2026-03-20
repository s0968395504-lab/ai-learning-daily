# -*- coding: utf-8 -*-
"""
Gemini OAuth Token 生成腳本
使用 client_secret.json 生成可用的 token.json
"""

import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# 設定 OAuth scopes
SCOPES = [
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/generative-language.retriever'
]

# 檔案路徑
CLIENT_SECRET_FILE = r"C:\Users\User\Desktop\client_secret_2_25974951072-620ij1dl997j4of3ou6jaqi60nhc6bda.apps.googleusercontent.com.json"
TOKEN_FILE = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "token.json")

def load_creds():
    """從 client_secret.json 生成 token.json"""
    creds = None
    
    # 檢查是否有現有的 token
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        print(f"✅ 找到現有 token 檔案")
    
    # 如果 token 無效，重新認證
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔄 刷新 token...")
            creds.refresh(Request())
        else:
            print("🔐 開始 OAuth 認證流程...")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # 保存 token
        os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
        with open(TOKEN_FILE, 'w', encoding='utf-8') as token:
            token.write(creds.to_json())
        print(f"✅ Token 已保存到：{TOKEN_FILE}")
    
    # 顯示 token 資訊
    print(f"\n📊 Token 狀態:")
    print(f"   - 有效：{creds.valid}")
    print(f"   - 過期：{creds.expired}")
    print(f"   - 有 refresh_token: {bool(creds.refresh_token)}")
    
    return creds

if __name__ == "__main__":
    try:
        creds = load_creds()
        print("\n✅ OAuth 认证成功！")
        print(f"Token 檔案位置：{TOKEN_FILE}")
        print("\n現在你可以使用 Gemini CLI 了！")
    except Exception as e:
        print(f"\n❌ 认证失敗：{e}")
        import traceback
        traceback.print_exc()
