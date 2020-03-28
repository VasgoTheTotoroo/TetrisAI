test = {
  'name': 'number_holes',
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
          >>> number_holes(board)
          4
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
