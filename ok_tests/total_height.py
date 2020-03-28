test = {
  'name': 'total_height',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> board = Board([[0, 0, 0, 1, 1, 1],
          ...                [0, 0, 0, 0, 0, 0],
          ...                [0, 1, 1, 1, 1, 1],
          ...                [0, 1, 1, 1, 1, 1],
          ...                [0, 1, 0, 1, 0, 1],
          ...                [1, 1, 1, 1, 1, 1],
          ...                [1, 0, 0, 1, 1, 1],
          ...                [0, 1, 1, 1, 1, 1],
          ...                [0, 0, 1, 1, 1, 1],
          ...                [0, 0, 1, 1, 1, 1],
          ...                [0, 1, 1, 1, 1, 1]]);
          >>> total_height(board)
          48
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
