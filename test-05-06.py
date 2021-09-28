import urllib.request
import bs4

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")

headline_news_div = bs_obj.find("div", {"class":"hdline_news"})
headline_article_div = bs_obj.find("ul", {"class":"hdline_article_list"})

headline_news = headline_news_div.findAll("p")
headline_article = headline_article_div.findAll("li");
for news in headline_news:
    print(news.text)

for article in headline_article:
    a_tag = article.find("a", {"class":"lnk_hdline_article"})
    print(a_tag.text.strip())

# <div class="main_component droppable" id="today_main_news">
        #     <div class="com_header">
        #         <h4 class="tit_h4 tit_main1"><strong>헤드라인 뉴스</strong></h4>
        #         <p class="news_info_txt">헤드라인 뉴스와 각 기사묶음 타이틀은 기사 내용을 기반으로 <strong>자동 추출</strong>됩니다.</p>
        #     </div>
        #     <!-- [D] 구형: .com_list.com_list_headline, 이시각주요뉴스:.newsnow, 헤드라인뉴스:.hdline_news -->
        #     <div class="hdline_news">
        #         <div class="hdline_flick">
        #             <div class="hdline_flick_item" style="display:block">
        #                 <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=100&amp;oid=437&amp;aid=0000276672" class="lnk_hdline_main_article nclicks('mai.image', '08138260_000000000000000000276672', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                     <img src="https://imgnews.pstatic.net/image/437/2021/09/23/0000276672_001_20210923145824387.jpg?type=nf300_190" width="300" height="190" alt="'대장동' 정조준한 국민의힘, 국정조사·특검법 제출…민주당은 '거부'" onerror="javascript:this.src='https://ssl.pstatic.net/static.news/image/news/2009/noimage_300x190.png';">
        #                     <div class="hdline_flick_mask">
        #                         <p class="hdline_flick_tit">'대장동' 정조준한 국민의힘, 국정조사·특검법 …</p>
        #                     </div>
        #                 </a>
                        
        #                     <a href="/main/clusterArticles.naver?id=c_202109231000_00000090&amp;mode=LSD&amp;mid=shm&amp;oid=437&amp;aid=0000276672" class="lnk_hdline_cluster_more nclicks('mai.clu', '08138260_000000000000000000276672', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                         <span class="blind">관련기사 개수</span>
        #                         <span class="cluster_more_icon_num">37</span>
        #                     </a>
                        
        #             </div>

        #             <div class="hdline_flick_item" style="display:none">
        #                 <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=102&amp;oid=032&amp;aid=0003099459" class="lnk_hdline_main_article nclicks('mai.image', '8800006B_000000000000000003099459', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                     <img src="https://imgnews.pstatic.net/image/032/2021/09/23/0003099459_001_20210923120106534.jpg?type=nf300_190" width="300" height="190" alt="내일부터 아동·청소년 온라인 그루밍 처벌한다…위장수사도 가능" onerror="javascript:this.src='https://ssl.pstatic.net/static.news/image/news/2009/noimage_300x190.png';">
        #                     <div class="hdline_flick_mask">
        #                         <p class="hdline_flick_tit">내일부터 아동·청소년 온라인 그루밍 처벌한다…</p>
        #                     </div>
        #                 </a>
                        
        #                     <a href="/main/clusterArticles.naver?id=c_202109211350_00000052&amp;mode=LSD&amp;mid=shm&amp;oid=032&amp;aid=0003099459" class="lnk_hdline_cluster_more nclicks('mai.clu', '8800006B_000000000000000003099459', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                         <span class="blind">관련기사 개수</span>
        #                         <span class="cluster_more_icon_num">39</span>
        #                     </a>
                        
        #             </div>

        #             <div class="hdline_flick_navi">
        #                 <button type="button" class="flick_btn_prev nclicks(mai.prev)" disabled="disabled" onclick="prevRecommend(); "><span class="blind">이전기사</span></button><button type="button" class="flick_btn_next nclicks(mai.next)" onclick="nextRecommend(); "><span class="blind">다음기사</span></button>
        #             </div> <!--[D] 버튼 비활성: disabled 속성 추가 -->
        #         </div>

        #         <ul class="hdline_article_list">
                    
                        
        #                     <li>
        #                         <div class="hdline_article_tit">
        #                             <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=100&amp;oid=016&amp;aid=0001890497" class="lnk_hdline_article nclicks('mai.text1', '8800010E_000000000000000001890497', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 문 대통령 “종전선언, 새 희망과 용기”...실현까지는 첩첩산중
        #                             </a>
        #                         </div>
        #                         <div class="hdline_cluster_more">
        #                             <a href="/main/clusterArticles.naver?id=c_202109230610_00000015&amp;mode=LSD&amp;mid=shm&amp;oid=016&amp;aid=0001890497" class="lnk_hdline_cluster_more nclicks('mai.clu', '8800010E_000000000000000001890497', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 <span class="blind">관련기사 개수</span>
        #                                 <span class="cluster_more_icon_num">40</span>
        #                             </a>
        #                         </div>
        #                     </li>
                        
                        
                    
                        
        #                     <li>
        #                         <div class="hdline_article_tit">
        #                             <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=102&amp;oid=079&amp;aid=0003555434" class="lnk_hdline_article nclicks('mai.text1', '88000112_000000000000000003555434', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 우석대, 수소융합얼라이언스·SZU와 업무협약
        #                             </a>
        #                         </div>
        #                         <div class="hdline_cluster_more">
        #                             <a href="/main/clusterArticles.naver?id=c_202109220940_00000001&amp;mode=LSD&amp;mid=shm&amp;oid=079&amp;aid=0003555434" class="lnk_hdline_cluster_more nclicks('mai.clu', '88000112_000000000000000003555434', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 <span class="blind">관련기사 개수</span>
        #                                 <span class="cluster_more_icon_num">48</span>
        #                             </a>
        #                         </div>
        #                     </li>
                        
                        
                    
                        
        #                     <li>
        #                         <div class="hdline_article_tit">
        #                             <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=102&amp;oid=088&amp;aid=0000722455" class="lnk_hdline_article nclicks('mai.text1', '880000C1_000000000000000000722455', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 [속보] 백신 접종완료자, 확진자 접촉해도 증상 없으면 격리면제
        #                             </a>
        #                         </div>
        #                         <div class="hdline_cluster_more">
        #                             <a href="/main/clusterArticles.naver?id=c_202109231430_00000002&amp;mode=LSD&amp;mid=shm&amp;oid=088&amp;aid=0000722455" class="lnk_hdline_cluster_more nclicks('mai.clu', '880000C1_000000000000000000722455', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 <span class="blind">관련기사 개수</span>
        #                                 <span class="cluster_more_icon_num">18</span>
        #                             </a>
        #                         </div>
        #                     </li>
                        
                        
                    
                        
        #                     <li>
        #                         <div class="hdline_article_tit">
        #                             <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=102&amp;oid=052&amp;aid=0001643438" class="lnk_hdline_article nclicks('mai.text1', '880000AF_000000000000000001643438', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                  "기분 나쁘니 좀 맞자"...만취한 남성 3명이 '묻지마 폭행'[제보는Y]
        #                             </a>
        #                         </div>
        #                         <div class="hdline_cluster_more">
        #                             <a href="/main/clusterArticles.naver?id=c_202109230900_00000229&amp;mode=LSD&amp;mid=shm&amp;oid=052&amp;aid=0001643438" class="lnk_hdline_cluster_more nclicks('mai.clu', '880000AF_000000000000000001643438', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 <span class="blind">관련기사 개수</span>
        #                                 <span class="cluster_more_icon_num">30</span>
        #                             </a>
        #                         </div>
        #                     </li>
                        
                        
                    
                        
        #                     <li>
        #                         <div class="hdline_article_tit">
        #                             <a href="/main/read.naver?mode=LSD&amp;mid=shm&amp;sid1=101&amp;oid=029&amp;aid=0002697782" class="lnk_hdline_article nclicks('mai.text1', '880000AD_000000000000000002697782', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 공항 소음 줄이고 피해 주민 수요 맞춘다
        #                             </a>
        #                         </div>
        #                         <div class="hdline_cluster_more">
        #                             <a href="/main/clusterArticles.naver?id=c_202109191650_00000193&amp;mode=LSD&amp;mid=shm&amp;oid=029&amp;aid=0002697782" class="lnk_hdline_cluster_more nclicks('mai.clu', '880000AD_000000000000000002697782', 'airsGParam', '0', 'news_global_v2.0', 'JoJ6s9TZUjrFTUHA')">
        #                                 <span class="blind">관련기사 개수</span>
        #                                 <span class="cluster_more_icon_num">19</span>
        #                             </a>
        #                         </div>
        #                     </li>
                        
                        
                    
        #         </ul>
        #     </div>

        #     <div class="btn_move">
        #         <!-- [D] .down_off 또는 .up_off 추가시 '<span class="blind">불가능</span>' 추가 -->
        #         <span class="move" title="이동">이동</span> <a href="#SLELq" class="nclicks(mai.up) up_off" title="위로">위로<span class="blind">불가능</span></a> <a href="#SLELq" class="nclicks(mai.down) down" title="아래로">아래로</a>
        #     </div>
        # </div>