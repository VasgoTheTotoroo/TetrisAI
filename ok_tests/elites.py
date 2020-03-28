test = {
  'name': 'elites',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.random.seed(42);
          >>> 
          >>> params = np.random.randn(10, 5);
          >>> scores = np.random.rand(10);
          >>> 
          >>> mean, std, best = elite_statistics(params, scores, 3);
          >>> 
          >>> np.round((mean, std, best), decimals=4)
          array([[-0.6724,  0.2584, -0.2927, -0.9019, -0.2243],
                 [ 0.4103,  1.0588,  1.1932,  0.3506,  0.8518],
                 [-0.5623, -1.0128,  0.3142, -0.908 , -1.4123]])
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
