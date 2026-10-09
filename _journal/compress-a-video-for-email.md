---
layout: journal
slug: compress-a-video-for-email
title: "How to compress a video for email: the size limits and the bitrate math"
date: 2026-07-25
seo:
  title: "How to Compress a Video for Email: Limits and Bitrate Math"
  description: "Gmail takes 25 MB, Outlook and iCloud Mail 20 MB. Why to aim below the limit, the bitrate that fits your clip, and how to do it on iPhone or Mac."
  keywords:
    - compress video for email
    - video too large to email
    - email attachment size limit
    - gmail attachment size limit
    - video bitrate for file size
    - mail drop size limit
    - compress video on iphone
    - mediakit
lede: "Every email provider caps what it will carry, and video reaches the cap fast. Here are the limits Gmail, Outlook and iCloud Mail publish, why a 25 MB limit does not take a 25 MB file, the arithmetic that turns a target size into a bitrate, and how MediaKit runs that arithmetic on iPhone or Mac without uploading the clip."
quick_answer: "To email a video, make the file smaller than your provider's limit with room to spare. Personal Gmail accepts 25 MB of attachments, the Outlook app 20 MB per message for internet accounts such as Outlook.com, iCloud Mail 20 MB, and Exchange work accounts 10 MB by default. Attachments travel Base64-encoded, which Microsoft says adds about 33%, so aim for about three-quarters of the limit: roughly 18 MB for Gmail and 15 MB for Outlook or iCloud Mail. To find the bitrate, multiply the target in megabytes by 8,000 and divide by the clip's length in seconds; that is the total in kbps. Subtract the audio bitrate (128 kbps is typical) and the rest is the video budget. Lower the resolution until the budget suits it, keep H.264 so the clip plays everywhere, and send a link instead when the budget gets too thin: Mail Drop carries up to 5 GB."
faq:
  - q: "What is the maximum video size you can email with Gmail?"
    a: "Personal Gmail accounts can send up to 25 MB of attachments in one message, counted together; work and school accounts follow limits set by their Google Workspace administrator. Above the limit, Gmail removes the attachment and adds it as a Google Drive link instead. Because attachments are Base64-encoded in transit, aim for a video of about 18 MB if it has to arrive as a real attachment."
  - q: "Why does my video bounce when it is under the attachment limit?"
    a: "Three common reasons. Attachments are Base64-encoded before they travel, and Microsoft's Exchange documentation says that adds about 33% to the message, so a file near the limit can exceed it once encoded. Some limits count the whole message, not just the attachment; Microsoft says Outlook's 20 MB limit includes the email. And the recipient's server has its own limit, which may be lower than yours, such as the 10 MB default on Exchange."
  - q: "How do I calculate the bitrate for a target file size?"
    a: "Multiply the target size in megabytes by 8,000 to get kilobits, divide by the clip's length in seconds to get the total bitrate in kbps, then subtract the audio bitrate. What remains is the video bitrate. For an 18 MB target and a 90-second clip: 18 × 8,000 = 144,000 kilobits, divided by 90 is 1,600 kbps, minus 128 kbps of audio leaves about 1,470 kbps for the picture."
  - q: "Should I use H.264 or HEVC for a video I am emailing?"
    a: "H.264 in an MP4, unless you know the recipient is on a recent Apple device. Apple says HEVC compresses better than H.264, so an HEVC file looks better at the same size, but you don't control what the attachment is opened on, and H.264 is the format almost everything plays. If the recipient is on a current iPhone, iPad or Mac, HEVC buys extra quality at the same size."
  - q: "What if my video is too long to compress small enough?"
    a: "Send a link. Mail Drop in Apple Mail and iCloud Mail sends files up to 5 GB as a download link that expires after 30 days, and Mail offers it when a message is too large for your provider. Gmail swaps an oversized attachment for a Google Drive link on its own. A five-minute clip squeezed into 15 MB leaves about 270 kbps for video, a quarter of what YouTube suggests even for 360p uploads."
  - q: "Can MediaKit compress a video to a specific file size?"
    a: "Yes. Video Compress has a Target size mode that takes a number in KB, MB or GB. MediaKit divides the target by the clip's length, takes out the audio bitrate you chose, holds back 3%, encodes, then measures the file it wrote and encodes again with a corrected bitrate if it missed. It runs on-device on iPhone and Mac, and Video Compress is one of five tools that stay free after the three-day trial."
mentioned_apps:
  - mediakit
read_time: "6 min read"
excerpt: "A reference for emailing video: the attachment limits Gmail, Outlook, Exchange, iCloud Mail and Mail Drop publish, why Base64 encoding means aiming for three-quarters of the limit, a bitrate table for clips from 30 seconds to five minutes, and how MediaKit's Target size mode runs the same arithmetic on iPhone and Mac."
---

At the 8 Mbps that YouTube recommends for 1080p uploads, one minute of video is 60 MB. That is more than twice what Gmail will attach. Getting a clip into an email is a small sum: pick a target below your provider's limit, work out the bitrate that fits it, and re-encode at that bitrate. Below are the numbers for each step, then how [MediaKit](/apps/mediakit/) does it on iPhone and Mac without sending the clip anywhere first.

## How big a video can you email?

| Service | Limit | What it counts | Over the limit |
|---|---|---|---|
| Gmail, personal account | 25 MB | All attachments in the message together | Gmail replaces the attachment with a Google Drive link |
| Outlook app, internet accounts such as Outlook.com | 20 MB | The attachments plus the email itself | Microsoft suggests compressing, or sharing a cloud link |
| Exchange, work accounts | 10 MB by default | The whole message; administrators can change it | As above |
| iCloud Mail | 20 MB | Incoming and outgoing messages | Up to 5 GB with Mail Drop turned on |
| Mail Drop (Apple Mail, iCloud Mail) | 5 GB | The message including attachments; each link expires after 30 days | Mail Drop can't send it |

Limits as each provider's help page stated them in July 2026: [Gmail Help](https://support.google.com/mail/answer/6584), [Microsoft Support](https://support.microsoft.com/en-us/office/send-large-files-with-outlook-8c698842-b462-4a4c-8d53-5c5dd04f77ef), and Apple's pages on [iCloud Mail limits](https://support.apple.com/en-us/102198) and [Mail Drop](https://support.apple.com/en-us/108329). Work and school accounts can be set lower by their administrators, and the receiving server applies its own limit. Microsoft's [Exchange documentation](https://learn.microsoft.com/en-us/exchange/mail-flow/message-size-limits) puts it plainly: a message must fit the limits of both sender and recipient. The smallest limit on the route is the one that counts.

## Why a 25 MB limit does not take a 25 MB file

Email is a text format. Before a video can travel as an attachment it is Base64-encoded: every three bytes of the file become four characters of text, broken into lines of at most 76 characters ([RFC 2045, section 6.8](https://www.rfc-editor.org/rfc/rfc2045#section-6.8)). The message that crosses the network is about a third larger than the file on your disk.

Whether a limit is measured before or after that encoding varies, and consumer help pages rarely say. Microsoft's Exchange documentation does: Base64 adds about 33%, so a 64 MB message limit means a realistic maximum of about 48 MB. Its Outlook page adds that the 20 MB limit includes the email, not just the attachment.

So the working rule is three-quarters of the stated limit:

| Stated limit | Aim for a file of about |
|---|---|
| 25 MB (Gmail) | 18 MB |
| 20 MB (Outlook, iCloud Mail) | 15 MB |
| 10 MB (Exchange default) | 7.5 MB |

Undershooting costs a little picture quality. Overshooting means a bounce, or a link where you wanted an attachment.

## How to work out the bitrate that fits

File size is bitrate multiplied by duration. Run it backwards:

1. **Convert the target to kilobits.** Megabytes × 8,000, counting a megabyte as 1,000,000 bytes.
2. **Divide by the clip's length in seconds.** That is the total bitrate in kbps.
3. **Subtract the audio.** 128 kbps is a common stereo setting; 64 kbps is plenty for speech.
4. **The rest is the video bitrate.** Leave a few percent for the container's own overhead.

A 90-second clip for Gmail: 18 MB × 8,000 = 144,000 kilobits. Divided by 90 seconds, that is 1,600 kbps. Take away 128 kbps of audio and about 1,470 kbps is left for the picture.

The same sum for common lengths, with 128 kbps of audio taken out first:

| Clip length | 7.5 MB file | 15 MB file | 18 MB file |
|---|---|---|---|
| 30 seconds | 1,870 kbps | 3,870 kbps | 4,670 kbps |
| 1 minute | 870 kbps | 1,870 kbps | 2,270 kbps |
| 2 minutes | 370 kbps | 870 kbps | 1,070 kbps |
| 5 minutes | 70 kbps | 270 kbps | 350 kbps |

Figures are rounded down.

## Which resolution and codec to choose

A bitrate is only generous or thin relative to the frame it has to fill. For scale, YouTube's [recommended upload settings](https://support.google.com/youtube/answer/1722171) for standard frame rates ask for 8 Mbps at 1080p, 5 Mbps at 720p, 2.5 Mbps at 480p and 1 Mbps at 360p. Those figures are high, because YouTube re-encodes everything it receives, but they show how fast the need falls with frame size: 1080p has 2.25 times the pixels of 720p.

A rough rule: if your video budget is well under half of YouTube's figure for the clip's resolution, step down one resolution. By that rule, a one-minute clip at 18 MB (2,270 kbps) sits better at 720p than at 1080p, and at 7.5 MB (870 kbps) it belongs at 480p or below. Three other settings move the result:

- **Audio bitrate.** For a talking-head clip, 64 kbps instead of 128 kbps hands the difference to the picture. On a five-minute clip at 15 MB, that is nearly a quarter more video bitrate.
- **Frame rate.** A 60 fps clip spreads its bits across twice as many frames as a 30 fps one. YouTube's figures for 48 to 60 fps are about half as high again as for 24 to 30.
- **Codec.** Apple says [HEVC compresses better than H.264](https://support.apple.com/en-us/116944), and recent Apple devices play it. But you don't control where the attachment is opened, and H.264 in an MP4 plays almost everywhere. Apple's page also notes that its devices *might* convert HEVC to H.264 when sharing to a device that can't play it; for a file you have already compressed, it is simpler to pick H.264 yourself.

## When to send a link instead

Compression has a floor, and the five-minute row of the table finds it: 270 kbps is about a quarter of what YouTube suggests for 360p. When the budget falls that low, a link serves the recipient better than an attachment.

- **Mail Drop** in Apple Mail and iCloud Mail sends files up to 5 GB as a download link that expires after 30 days. Mail offers it when a message is larger than your provider allows.
- **Gmail** swaps an attachment over 25 MB for a Google Drive link on its own.
- **Outlook** points you to compressing the file or sharing it from cloud storage.

The trade is simple: the recipient gets the full-quality original, and a copy sits on a server for as long as the link lives.

## Doing it in MediaKit

[MediaKit](/apps/mediakit/) runs the arithmetic above on the device, on iPhone and on Mac, and never uploads the clip. Video Compress is one of the five tools that stay free after the three-day trial.

1. **Open the clip.** On a Mac, drag it onto the window. On iPhone, add it from Photos or Files, or send it from another app's share sheet.
2. **Choose the video Compress tool** and set **Mode** to **Target size**.
3. **Type the target** from the three-quarters table, for example 18, with the unit on MB. MediaKit counts a megabyte as 1,000,000 bytes.
4. **Open Advanced.** Set **Max resolution** using the bitrate table, leave **Codec** on H.264 for email, and choose **64 kbps (voice)** under **Audio bitrate** if the clip is mostly speech.
5. **Run it, then check the size** of the result before you attach it.

In Target size mode MediaKit does steps one to four of the sum itself: it divides the target by the clip's length, takes out the audio bitrate you chose and holds back 3%, encodes, then measures the file it wrote and encodes again with a corrected bitrate if it missed. A 4K or 1440p source starts with Max resolution set to 1080p; for a small target, set it lower.

If you already use HandBrake for this job, the [HandBrake comparison](/alternatives/handbrake/) covers where the two differ, and the [Compress Videos & Resize Video comparison](/alternatives/compress-videos-resize-video/) does the same on iPhone. Why the studio keeps this work off other people's servers is the subject of [an earlier post](/journal/your-photos-shouldnt-ride-the-elevator/), and the wider toolkit is in [this one](/journal/every-media-tool-already-on-your-mac/).
