from silver_service_taxi import SilverServiceTaxi

def main():
    """Run tests for the SilverServiceTaxi class"""
    sst1 = SilverServiceTaxi(name="Toyota", fuel=100, fanciness=2)
    sst1.drive(18)
    print(sst1.get_fare())

main()