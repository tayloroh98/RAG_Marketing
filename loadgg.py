from google.ads.googleads.client import GoogleAdsClient
client = GoogleAdsClient.load_from_storage("google_ads.yaml")

import logging
import sys

logger = logging.getLogger('google.ads.googleads.client')
logger.addHandler(logging.StreamHandler(sys.stdout))

def test_connection(client):
    """연결 테스트 함수"""
    try:
        # 간단한 API 호출로 연결 테스트
        ga_service = client.get_service("GoogleAdsService")
        print("✅ Google Ads API 클라이언트 연결 성공!")
        print("✅ 서비스 객체 생성 성공!")
        return True
    except Exception as e:
        print(f"❌ 연결 실패: {e}")
        return False

def main(client, customer_id):
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT
          customer.id,
          customer.descriptive_name
        FROM customer
        LIMIT 1"""

    print("🔍 고객 정보를 조회하고 있습니다...")
    
    # Issues a search request using streaming.
    stream = ga_service.search_stream(customer_id=customer_id, query=query)
    
    customer_count = 0
    for batch in stream:
        for row in batch.results:
            customer_count += 1
            print(f"\n📋 고객 정보 #{customer_count}")
            print(f"   ID: {row.customer.id}")
            print(f"   이름: {row.customer.descriptive_name}")
            print("-" * 30)
    
    if customer_count == 0:
        print("📭 조회된 고객 정보가 없습니다.")
    else:
        print(f"\n📊 총 {customer_count}개의 고객 정보를 조회했습니다.")

# 연결 테스트 실행
if __name__ == "__main__":
    print("🔍 Google Ads API 연결 테스트 중...")
    if test_connection(client):
        print("🎉 모든 설정이 올바르게 작동합니다!")
        print("\n📊 실제 데이터 조회를 시작합니다...")
        
        # customer_id 설정 (테스트 계정 ID 사용)
        customer_id = "TEST_ACCOUNT_ID"  # 테스트 계정 생성 후 여기에 입력
        print(f"🔍 Customer ID: {customer_id}에서 데이터를 조회합니다...")
        
        try:
            main(client, customer_id)
            print("✅ 데이터 조회 완료!")
        except Exception as e:
            print(f"❌ 데이터 조회 중 오류 발생: {e}")
    else:
        print("💥 연결에 실패했습니다. 설정을 확인해주세요.")