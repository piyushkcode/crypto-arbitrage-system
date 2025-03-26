import unittest

def run_tests():
    """
    Discover and run all tests in the project
    
    :return: Test runner result
    """
    # Create a test loader and test runner
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Discover tests in the current directory
    suite = loader.discover('.')
    
    # Run the tests
    result = runner.run(suite)
    
    return result

__all__ = ['run_tests']