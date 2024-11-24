#!/bin/bash
mkdir -p ./tmp
ffmpeg -y -i samples/bee1920.mp4 -ss 10 -t 2 -r 30 ./tmp/clip1.mp4
ffmpeg -y -i samples/book1920.mp4 -ss 5 -t 1 -r 30 ./tmp/clip2.mp4
ffmpeg -y -i samples/cows1920.mp4 -ss 3 -t 5 -r 30 ./tmp/clip3.mp4
ffmpeg -y -i samples/bee1920.mp4 -ss 27 -t 5 -r 30 ./tmp/clip4.mp4
ffmpeg -y -i samples/book1920.mp4 -ss 0 -t 5 -r 30 ./tmp/clip5.mp4
ffmpeg -y -i samples/flowers1920.mp4 -ss 15 -t 5 -r 30 ./tmp/clip6.mp4
ffmpeg -y -i samples/cows1920.mp4 -ss 0 -t 5 -r 30 ./tmp/clip7.mp4
ffmpeg -y -i samples/bee1920.mp4 -ss 0 -t 5 -r 30 ./tmp/clip8.mp4
ffmpeg -y \
-i ./tmp/clip1.mp4 \
-i ./tmp/clip2.mp4 \
-i ./tmp/clip3.mp4 \
-i ./tmp/clip4.mp4 \
-i ./tmp/clip5.mp4 \
-i ./tmp/clip6.mp4 \
-i ./tmp/clip7.mp4 \
-i ./tmp/clip8.mp4 \
-i samples/ever.mp3 \
-i samples/weekend.mp3 \
-i samples/flower.png \
-filter_complex "color=c=black:s=384x216:d=38[base];
color=c=black@0.0:s=384x216:d=3[gap_aUyVdzH8];
color=black@0.0:s=384x216:d=2[S8Q59xh6_base];
[0:v]scale=384:216,format=rgba,colorchannelmixer=aa=1[iMtdrLC6_clip];
[S8Q59xh6_base][iMtdrLC6_clip]overlay=0:0:format=auto,rotate=0,fps=30[clip1];
color=black@0.0:s=384x216:d=1[eo9VYadF_base];
[1:v]scale=384:216,format=rgba,colorchannelmixer=aa=1[pKMiULsZ_clip];
[eo9VYadF_base][pKMiULsZ_clip]overlay=0:0:format=auto,rotate=0,fps=30[clip2];
color=c=black@0.0:s=384x216:d=4[gap_TBr3mgKD];
color=black@0.0:s=384x216:d=5[ILix2C8i_base];
[2:v]scale=192:108,format=rgba,colorchannelmixer=aa=0.5[kycGyw1b_clip];
[ILix2C8i_base][kycGyw1b_clip]overlay=96:54:format=auto,rotate=45,fps=30[clip3];
color=black@0.0:s=384x216:d=5[6vpLn5zv_base];
[3:v]scale=384:216,format=rgba,colorchannelmixer=aa=1[rq7nwVMH_clip];
[6vpLn5zv_base][rq7nwVMH_clip]overlay=0:0:format=auto,rotate=0,fps=30[clip4];
color=black@0.0:s=384x216:d=5[9kiATaXe_base];
[4:v]scale=80:60,format=rgba,colorchannelmixer=aa=1[fAv1pdxL_clip];
[9kiATaXe_base][fAv1pdxL_clip]overlay=10:10:format=auto,rotate=0,fps=30[clip5];
color=black@0.0:s=384x216:d=5[E5nPjCVW_base];
[5:v]scale=384:216,format=rgba,colorchannelmixer=aa=1[GjOFdzfS_clip];
[E5nPjCVW_base][GjOFdzfS_clip]overlay=0:0:format=auto,rotate=0,fps=30[clip6];
color=black@0.0:s=384x216:d=5[HRBO3ll4_base];
[6:v]scale=384:216,format=rgba,colorchannelmixer=aa=1[DdCUtc5e_clip];
[HRBO3ll4_base][DdCUtc5e_clip]overlay=0:0:format=auto,rotate=0,fps=30[clip7];
color=black@0.0:s=384x216:d=5[yt4rY1yX_base];
[7:v]scale=384:216,format=rgba,colorchannelmixer=aa=1[eKjWZEDg_clip];
[yt4rY1yX_base][eKjWZEDg_clip]overlay=0:0:format=auto,rotate=0,fps=30[clip8];
color=c=black@0.0:s=384x216:d=0.5[void_clip1];
[void_clip1]fps=30[fps_void_clip1_3Yaojvpz];
[clip1]fps=30[fps_clip1_iXc58w6w];
[fps_void_clip1_3Yaojvpz][fps_clip1_iXc58w6w]xfade=transition=smoothup:duration=0.43333333333333335:offset=0,fps=30[start_xfade_HMfaKp6U];
color=c=black@0.0:s=384x216:d=0.5[void_start_xfade_HMfaKp6U];
[start_xfade_HMfaKp6U]fps=30[fps_start_xfade_HMfaKp6U_IqSDXixZ];
[void_start_xfade_HMfaKp6U]fps=30[fps_void_start_xfade_HMfaKp6U_q8BTRiDq];
[fps_start_xfade_HMfaKp6U_IqSDXixZ][fps_void_start_xfade_HMfaKp6U_q8BTRiDq]xfade=transition=smoothdown:duration=0.43333333333333335:offset=1.5,fps=30[end_xfade_KlxmaoAm];
color=c=black@0.0:s=384x216:d=0.5[void_clip2];
[void_clip2]fps=30[fps_void_clip2_gIaxDA0N];
[clip2]fps=30[fps_clip2_GM1nXdZF];
[fps_void_clip2_gIaxDA0N][fps_clip2_GM1nXdZF]xfade=transition=fade:duration=0.43333333333333335:offset=0,fps=30[start_xfade_PedvU5ny];
color=c=black@0.0:s=384x216:d=0.5[void_start_xfade_PedvU5ny];
[start_xfade_PedvU5ny]fps=30[fps_start_xfade_PedvU5ny_VmiNzMAv];
[void_start_xfade_PedvU5ny]fps=30[fps_void_start_xfade_PedvU5ny_snR45pjV];
[fps_start_xfade_PedvU5ny_VmiNzMAv][fps_void_start_xfade_PedvU5ny_snR45pjV]xfade=transition=circlecrop:duration=0.43333333333333335:offset=0.5,fps=30[end_xfade_Ys3Ia7Xy];
color=c=black@0.0:s=384x216:d=0.5[void_clip3];
[clip3]fps=30[fps_clip3_C70rIJQT];
[void_clip3]fps=30[fps_void_clip3_Vg1cWolZ];
[fps_clip3_C70rIJQT][fps_void_clip3_Vg1cWolZ]xfade=transition=squeezev:duration=0.43333333333333335:offset=4.5,fps=30[end_xfade_2ipldqOt];
color=c=black@0.0:s=384x216:d=0.5[void_clip8];
[clip8]fps=30[fps_clip8_xqsyDffv];
[void_clip8]fps=30[fps_void_clip8_xGV8tr59];
[fps_clip8_xqsyDffv][fps_void_clip8_xGV8tr59]xfade=transition=smoothdown:duration=0.43333333333333335:offset=4.5,fps=30[end_xfade_cVuDhlpj];
[gap_aUyVdzH8][end_xfade_KlxmaoAm]concat=n=2:v=1:a=0,fps=30[between_concat_rZiL9evH];
[between_concat_rZiL9evH][end_xfade_Ys3Ia7Xy]concat=n=2:v=1:a=0,fps=30[between_concat_nYvzXr16];
[between_concat_nYvzXr16][gap_TBr3mgKD]concat=n=2:v=1:a=0,fps=30[between_concat_X84ttSkI];
[between_concat_X84ttSkI][end_xfade_2ipldqOt]concat=n=2:v=1:a=0,fps=30[between_concat_RHfh0DGw];
[between_concat_RHfh0DGw][clip4]concat=n=2:v=1:a=0,fps=30[between_concat_4i5V28yh];
[between_concat_4i5V28yh]fps=30[fps_between_concat_4i5V28yh_7HpMWnZW];
[clip5]fps=30[fps_clip5_AaXNy2O9];
[fps_between_concat_4i5V28yh_7HpMWnZW][fps_clip5_AaXNy2O9]xfade=transition=fade:duration=1:offset=19,fps=30[between_xfade_kwpugYtf];
[between_xfade_kwpugYtf]fps=30[fps_between_xfade_kwpugYtf_l8Qys9aI];
[clip6]fps=30[fps_clip6_rizR8ELX];
[fps_between_xfade_kwpugYtf_l8Qys9aI][fps_clip6_rizR8ELX]xfade=transition=smoothdown:duration=1:offset=23,fps=30[between_xfade_z1XngxIq];
[between_xfade_z1XngxIq][clip7]concat=n=2:v=1:a=0,fps=30[between_concat_LuscXdfZ];
[between_concat_LuscXdfZ][end_xfade_cVuDhlpj]concat=n=2:v=1:a=0,fps=30[track_with_some_videos];
color=black@0.0:s=384x216:d=30[bLSODmof_base];
[10:v]loop=loop=900:size=900,setpts=PTS-STARTPTS,fps=30,scale=60:30,format=rgba,colorchannelmixer=aa=1[y0n7OGMz_clip];
[bLSODmof_base][y0n7OGMz_clip]overlay=322:2:format=auto,rotate=0,fps=30[watermark_clip];
color=c=black@0.0:s=384x216:d=8[gap_D90KOMpj];
color=c=black@0.0:s=384x216:d=0.5[void_watermark_clip];
[watermark_clip]fps=30[fps_watermark_clip_q781PDoH];
[void_watermark_clip]fps=30[fps_void_watermark_clip_fEvy0RZc];
[fps_watermark_clip_q781PDoH][fps_void_watermark_clip_fEvy0RZc]xfade=transition=squeezeh:duration=0.43333333333333335:offset=29.5,fps=30[end_xfade_2zICpUZW];
[end_xfade_2zICpUZW][gap_D90KOMpj]concat=n=2:v=1:a=0,fps=30[track_with_watermark];
anullsrc=channel_layout=stereo:sample_rate=44100:d=5[gap_4lv0SECH];
[8:a]atrim=0:10,asetpts=PTS-STARTPTS,volume=1[audio_clip1];
anullsrc=channel_layout=stereo:sample_rate=44100:d=5[gap_rqh0ycJz];
[9:a]atrim=0:15,asetpts=PTS-STARTPTS,volume=1[audio_clip2];
anullsrc=channel_layout=stereo:sample_rate=44100:d=3[gap_SjfgojYq];
[gap_4lv0SECH][audio_clip1][gap_rqh0ycJz][audio_clip2][gap_SjfgojYq]concat=n=5:v=0:a=1[track2];
[base][track_with_some_videos]overlay=0:0[roPveNf4_combined_track];
[roPveNf4_combined_track][track_with_watermark]overlay=0:0[video_output];
[track2]volume=1[audio_output];" \
-map '[video_output]' -map '[audio_output]' -c:v libx264 -c:a aac -b:a 320k -r 30 -s 384x216 -ss 0 -t 38 -crf 23 -preset veryfast -pix_fmt yuv420p output.mp4