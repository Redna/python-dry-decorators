import logging

from python_dry_decorators.example import another, always_failing, finally_passing, runtime_error_failing


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)20s :: %(levelname)-8s :: %(name)s :: %(message)s', level=logging.DEBUG)
    print(f"finished {another(dict(demo= 5), call_count=5)}")

    print("next one")

    print(f"finished {another(dict(demo= 5), call_count=3)}")


    try:
        always_failing()
    except:
        print("always failing fails always.. Wow")

    try: 
        runtime_error_failing()
    except:
        print("runtime_error_failing: That was excpected..")
    
    finally_passing()


    print(always_failing())
