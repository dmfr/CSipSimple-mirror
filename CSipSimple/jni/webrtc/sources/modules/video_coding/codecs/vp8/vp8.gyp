# Copyright (c) 2012 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'includes': [
    '../../../../build/common.gypi',
    '../test_framework/test_framework.gypi'
  ],
  'targets': [
    {
      'target_name': 'webrtc_vp8',
      'type': '<(library)',
      'dependencies': [
        '<(webrtc_root)/system_wrappers/source/system_wrappers.gyp:system_wrappers',
        '<(webrtc_root)/common_video/common_video.gyp:common_video',
      ],
      'include_dirs': [
        'include',
        '<(webrtc_root)/common_video/interface',
        '<(webrtc_root)/modules/video_coding/codecs/interface',
        '<(webrtc_root)/modules/interface',
      ],
      'conditions': [
        ['build_libvpx==1', {
          'dependencies': [
            '<(DEPTH)/third_party/libvpx/libvpx.gyp:libvpx',
          ],
        }],
        # TODO(mikhal): Investigate this mechanism for handling differences
        # between the Chromium and standalone builds.
        # http://code.google.com/p/webrtc/issues/detail?id=201
        ['build_with_chromium==1', {
          'defines': [
            'WEBRTC_LIBVPX_VERSION=960' # Bali
          ],
        }, {
          'defines': [
            'WEBRTC_LIBVPX_VERSION=971' # Cayuga
          ],
          'sources': [
            'temporal_layers.h',
            'temporal_layers.cc',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
          '<(webrtc_root)/common_video/interface',
          '<(webrtc_root)/modules/video_coding/codecs/interface',
        ],
      },
      'sources': [
        'reference_picture_selection.h',
        'reference_picture_selection.cc',
        'include/vp8.h',
        'include/vp8_common_types.h',
        'vp8_impl.cc',
      ],
    },
  ], # targets
  'conditions': [
    ['include_tests==1', {
      'targets': [
        {
          'target_name': 'vp8_integrationtests',
          'type': 'executable',
          'dependencies': [
            'test_framework',
            'webrtc_vp8',
            '<(webrtc_root)/common_video/common_video.gyp:common_video',
            '<(webrtc_root)/system_wrappers/source/system_wrappers.gyp:system_wrappers',
            '<(webrtc_root)/test/test.gyp:test_support',
            '<(webrtc_root)/test/test.gyp:test_support_main',
            '<(DEPTH)/testing/gtest.gyp:gtest',
          ],
         'sources': [
            # header files
            'test/benchmark.h',
            'test/dual_decoder_test.h',
            'test/normal_async_test.h',
            'test/packet_loss_test.h',
            'test/rps_test.h',
            'test/vp8_unittest.h',

           # source files
            'test/benchmark.cc',
            'test/dual_decoder_test.cc',
            'test/normal_async_test.cc',
            'test/packet_loss_test.cc',
            'test/rps_test.cc',
            'test/tester.cc',
            'test/vp8_unittest.cc',
          ],
        },
        {
          'target_name': 'vp8_unittests',
          'type': 'executable',
          'dependencies': [
            'webrtc_vp8',
            '<(DEPTH)/testing/gmock.gyp:gmock',
            '<(DEPTH)/testing/gtest.gyp:gtest',
            '<(webrtc_root)/test/test.gyp:test_support_main',
          ],
          'include_dirs': [
            '<(DEPTH)/third_party/libvpx/source/libvpx',
          ],
          'sources': [
            'reference_picture_selection_unittest.cc',
            'temporal_layers_unittest.cc',
          ],
          'conditions': [
            ['build_libvpx==1', {
              'dependencies': [
                '<(DEPTH)/third_party/libvpx/libvpx.gyp:libvpx',
              ],
            }],
          ],
        },
      ], # targets
    }], # include_tests
  ],
}
