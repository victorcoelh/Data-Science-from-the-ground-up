import pytest

from src.probability import Distributions


class TestDistributions:
    def test_uniform_pdf(self):
        assert Distributions.uniform_pdf(-1) == 0
        assert Distributions.uniform_pdf(0) == 1
        assert Distributions.uniform_pdf(1) == 1
        assert Distributions.uniform_pdf(2) == 0
    
    def test_uniform_cdf(self):
        assert Distributions.uniform_cdf(0) == 0
        assert Distributions.uniform_cdf(0.5) == 0.5
        assert Distributions.uniform_cdf(1) == 1
        assert Distributions.uniform_cdf(2) == 1
    
    def test_normal_pdf(self):
        assert Distributions.normal_pdf(0, 0, 1) == pytest.approx(0.398942, 0.01)
        assert Distributions.normal_pdf(-0.5, -1, 0.5) == pytest.approx(0.483942, 0.01)
    
    def test_normal_cdf(self):
        assert Distributions.normal_cdf(0.7, 0, 1) == pytest.approx(0.758036, 0.01)
        assert Distributions.normal_cdf(0, -1, 0.5) == pytest.approx(0.977249, 0.01)
    
    #TODO: test inverse cdf
    def test_inverse_normal_cdf(self):
        pass
    
    #TODO: find a way to test bernoulli trial and binomial (random values)
    def test_bernoulli_trial(self):
        pass
    
    def test_binomial(self):
        pass
