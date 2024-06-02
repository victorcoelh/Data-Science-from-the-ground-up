import pytest

from src.probability import Distributions, NormalProbability


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
    

class TestNormalProbability:
    def test_below(self):
        assert NormalProbability.below(1.5, 1, 1) == pytest.approx(0.69146, 0.01)
        assert NormalProbability.below(2, 0, 2) == pytest.approx(0.84134, 0.01)
    
    def test_above(self):
        assert NormalProbability.above(1.5, 1, 1) == pytest.approx(0.30853, 0.01)
        assert NormalProbability.above(2, 0, 2) == pytest.approx(0.15865, 0.01)
    
    def test_between(self):
        assert NormalProbability.between(-0.5, 0.5, 0, 1) == pytest.approx(0.38292, 0.01)
        assert NormalProbability.between(0, 1, 0, 2) == pytest.approx(0.19146, 0.01)
    
    def test_outside(self):
        assert NormalProbability.outside(-0.5, 0.5, 1, 1) == pytest.approx(0.75826, 0.01)
        assert NormalProbability.outside(0, 1, 0, 2) == pytest.approx(0.80853, 0.01)
    
    def test_upper_bound(self):
        assert NormalProbability.upper_bound(0.3, 0, 1) == pytest.approx(-0.524, 0.01)
        assert NormalProbability.upper_bound(0.7, 0, 1) == pytest.approx(0.524, 0.01)
    
    def test_lower_bound(self):
        assert NormalProbability.lower_bound(0.4, 0, 1) == pytest.approx(0.253, 0.01)
        assert NormalProbability.lower_bound(0.9, 0, 1) == pytest.approx(-1.282, 0.01)
    
    def test_two_sided_bound(self):
        assert NormalProbability.two_sided_bound(0.2, 0, 1) == pytest.approx(0.253, 0.01)
        assert NormalProbability.two_sided_bound(0.95, 0, 1) == pytest.approx(1.96, 0.01)
