from silver_service_taxi import SilverServiceTaxi
EXPECTED_FARE = 48.78

def main():
    """Run tests for the SilverServiceTaxi class"""
    sst1 = SilverServiceTaxi(name="Toyota", fuel=100, fanciness=2)
    sst1.drive(18)
    #print(sst1.get_fare())
    assert sst1.get_fare() == EXPECTED_FARE, f"Fare expected: ${EXPECTED_FARE}, got: ${sst1.get_fare()}"

main()