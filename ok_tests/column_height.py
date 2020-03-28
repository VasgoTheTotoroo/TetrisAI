test = {
  'name': 'column_height',
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
          >>> column_height(board.grid.T)
          array([3, 0, 5, 5, 5, 6, 6, 5, 4, 4, 5])
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
