test = {
  'name': 'complete_lines',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> board = Board([[0, 0, 0, 1, 1, 1],
          ...                [0, 1, 1, 1, 1, 1],
          ...                [0, 1, 1, 1, 1, 1],
          ...                [0, 1, 0, 1, 0, 1],
          ...                [1, 1, 1, 1, 1, 1],
          ...                [1, 0, 0, 1, 1, 1],
          ...                [0, 1, 1, 1, 1, 1],
          ...                [0, 0, 1, 1, 1, 1],
          ...                [0, 0, 1, 1, 1, 1],
          ...                [0, 1, 1, 1, 1, 1]]);
          >>> complete_lines(board)
          2
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
