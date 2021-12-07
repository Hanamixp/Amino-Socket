
class RankingTableList:
    def __init__(self, data):
        self.json = data
        self.title = []
        self.level = []
        self.reputation = []
        self.id = []

    @property
    def RankingTableList(self):
        for x in self.json:
            try: self.title.append(x["title"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.level.append(x["level"])
            except (KeyError, TypeError): self.level.append(None)
            try: self.reputation.append(x["reputation"])
            except (KeyError, TypeError): self.reputation.append(None)
            try: self.id.append(x["id"])
            except (KeyError, TypeError): self.id.append(None)

        return self


class Community:
    def __init__(self, data):
        self.json = data

        try: self.agent: UserProfile = UserProfile(data["agent"]).UserProfile
        except (KeyError, TypeError): self.agent: UserProfile = UserProfile([])
        try: self.rankingTable: RankingTableList = RankingTableList(data["advancedSettings"]["rankingTable"]).RankingTableList
        except (KeyError, TypeError): self.rankingTable: RankingTableList = RankingTableList([])

        self.usersCount = None
        self.createdTime = None
        self.aminoId = None
        self.icon = None
        self.link = None
        self.comId = None
        self.modifiedTime = None
        self.status = None
        self.joinType = None
        self.tagline = None
        self.primaryLanguage = None
        self.heat = None
        self.themePack = None
        self.probationStatus = None
        self.listedStatus = None
        self.userAddedTopicList = None
        self.name = None
        self.isStandaloneAppDeprecated = None
        self.searchable = None
        self.influencerList = None
        self.keywords = None
        self.mediaList = None
        self.description = None
        self.isStandaloneAppMonetizationEnabled = None
        self.advancedSettings = None
        self.activeInfo = None
        self.configuration = None
        self.extensions = None
        self.nameAliases = None
        self.templateId = None
        self.promotionalMediaList = None
        self.defaultRankingTypeInLeaderboard = None
        self.joinedBaselineCollectionIdList = None
        self.newsfeedPages = None
        self.catalogEnabled = None
        self.pollMinFullBarVoteCount = None
        self.leaderboardStyle = None
        self.facebookAppIdList = None
        self.welcomeMessage = None
        self.welcomeMessageEnabled = None
        self.hasPendingReviewRequest = None
        self.frontPageLayout = None
        self.themeColor = None
        self.themeHash = None
        self.themeVersion = None
        self.themeUrl = None
        self.themeHomePageAppearance = None
        self.themeLeftSidePanelTop = None
        self.themeLeftSidePanelBottom = None
        self.themeLeftSidePanelColor = None
        self.customList = None

    @property
    def Community(self):
        try: self.name = self.json["name"]
        except (KeyError, TypeError): pass
        try: self.usersCount = self.json["membersCount"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.aminoId = self.json["endpoint"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.link = self.json["link"]
        except (KeyError, TypeError): pass
        try: self.comId = self.json["ndcId"]
        except (KeyError, TypeError): pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.joinType = self.json["joinType"]
        except (KeyError, TypeError): pass
        try: self.primaryLanguage = self.json["primaryLanguage"]
        except (KeyError, TypeError): pass
        try: self.heat = self.json["communityHeat"]
        except (KeyError, TypeError): pass
        try: self.userAddedTopicList = self.json["userAddedTopicList"]
        except (KeyError, TypeError): pass
        try: self.probationStatus = self.json["probationStatus"]
        except (KeyError, TypeError): pass
        try: self.listedStatus = self.json["listedStatus"]
        except (KeyError, TypeError): pass
        try: self.themePack = self.json["themePack"]
        except (KeyError, TypeError): pass
        try: self.themeColor = self.json["themePack"]["themeColor"]
        except (KeyError, TypeError): pass
        try: self.themeHash = self.json["themePack"]["themePackHash"]
        except (KeyError, TypeError): pass
        try: self.themeVersion = self.json["themePack"]["themePackRevision"]
        except (KeyError, TypeError): pass
        try: self.themeUrl = self.json["themePack"]["themePackUrl"]
        except (KeyError, TypeError): pass
        try: self.themeHomePageAppearance = self.json["configuration"]["appearance"]["homePage"]["navigation"]
        except (KeyError, TypeError): pass
        try: self.themeLeftSidePanelTop = self.json["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level1"]
        except (KeyError, TypeError): pass
        try: self.themeLeftSidePanelBottom = self.json["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level2"]
        except (KeyError, TypeError): pass
        try: self.themeLeftSidePanelColor = self.json["configuration"]["appearance"]["leftSidePanel"]["style"]["iconColor"]
        except (KeyError, TypeError): pass
        try: self.customList = self.json["configuration"]["page"]["customList"]
        except (KeyError, TypeError): pass
        try: self.tagline = self.json["tagline"]
        except (KeyError, TypeError): pass
        try: self.searchable = self.json["searchable"]
        except (KeyError, TypeError): pass
        try: self.isStandaloneAppDeprecated = self.json["isStandaloneAppDeprecated"]
        except (KeyError, TypeError): pass
        try: self.influencerList = self.json["influencerList"]
        except (KeyError, TypeError): pass
        try: self.keywords = self.json["keywords"]
        except (KeyError, TypeError): pass
        try: self.mediaList = self.json["mediaList"]
        except (KeyError, TypeError): pass
        try: self.description = self.json["content"]
        except (KeyError, TypeError): pass
        try: self.isStandaloneAppMonetizationEnabled = self.json["isStandaloneAppMonetizationEnabled"]
        except (KeyError, TypeError): pass
        try: self.advancedSettings = self.json["advancedSettings"]
        except (KeyError, TypeError): pass
        try: self.defaultRankingTypeInLeaderboard = self.json["advancedSettings"]["defaultRankingTypeInLeaderboard"]
        except (KeyError, TypeError): pass
        try: self.frontPageLayout = self.json["advancedSettings"]["frontPageLayout"]
        except (KeyError, TypeError): pass
        try: self.hasPendingReviewRequest = self.json["advancedSettings"]["hasPendingReviewRequest"]
        except (KeyError, TypeError): pass
        try: self.welcomeMessageEnabled = self.json["advancedSettings"]["welcomeMessageEnabled"]
        except (KeyError, TypeError): pass
        try: self.welcomeMessage = self.json["advancedSettings"]["welcomeMessageText"]
        except (KeyError, TypeError): pass
        try: self.pollMinFullBarVoteCount = self.json["advancedSettings"]["pollMinFullBarVoteCount"]
        except (KeyError, TypeError): pass
        try: self.catalogEnabled = self.json["advancedSettings"]["catalogEnabled"]
        except (KeyError, TypeError): pass
        try: self.leaderboardStyle = self.json["advancedSettings"]["leaderboardStyle"]
        except (KeyError, TypeError): pass
        try: self.facebookAppIdList = self.json["advancedSettings"]["facebookAppIdList"]
        except (KeyError, TypeError): pass
        try: self.newsfeedPages = self.json["advancedSettings"]["newsfeedPages"]
        except (KeyError, TypeError): pass
        try: self.joinedBaselineCollectionIdList = self.json["advancedSettings"]["joinedBaselineCollectionIdList"]
        except (KeyError, TypeError): pass
        try: self.activeInfo = self.json["activeInfo"]
        except (KeyError, TypeError): pass
        try: self.configuration = self.json["configuration"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.nameAliases = self.json["extensions"]["communityNameAliases"]
        except (KeyError, TypeError): pass
        try: self.templateId = self.json["templateId"]
        except (KeyError, TypeError): pass
        try: self.promotionalMediaList = self.json["promotionalMediaList"]
        except (KeyError, TypeError): pass

        return self


class UserProfileList:
    def __init__(self, data):
        _fanClub = []

        self.json = data

        for y in data:
            try: _fanClub.append(FanClubList(y["fanClubList"]).FanClubList)
            except (KeyError, TypeError): _fanClub.append(None)

        self.accountMembershipStatus = []
        self.activation = []
        self.activePublicLiveThreadId = []
        self.age = []
        self.aminoId = []
        self.aminoIdEditable = []
        self.appleId = []
        self.avatarFrame = []
        self.avatarFrameId = []
        self.backgroundColor = []
        self.backgroundImage = []
        self.blogsCount = []
        self.commentsCount = []
        self.content = []
        self.coverAnimation = []
        self.createdTime = []
        self.customTitles = []
        self.dateOfBirth = []
        self.defaultBubbleId = []
        self.disabledLevel = []
        self.disabledStatus = []
        self.disabledTime = []
        self.email = []
        self.extensions = []
        self.facebookId = []
        self.fansCount = []
        self.fanClub = _fanClub
        self.followersCount = []
        self.followingCount = []
        self.followingStatus = []
        self.gender = []
        self.globalStrikeCount = []
        self.googleId = []
        self.icon = []
        self.influencerCreatedTime = []
        self.influencerInfo = []
        self.influencerMonthlyFee = []
        self.influencerPinned = []
        self.isGlobal = []
        self.isMemberOfTeamAmino = []
        self.isNicknameVerified = []
        self.itemsCount = []
        self.lastStrikeTime = []
        self.lastWarningTime = []
        self.level = []
        self.mediaList = []
        self.membershipStatus = []
        self.modifiedTime = []
        self.mood = []
        self.moodSticker = []
        self.nickname = []
        self.notificationSubscriptionStatus = []
        self.onlineStatus = []
        self.onlineStatus2 = []
        self.phoneNumber = []
        self.postsCount = []
        self.privilegeOfChatInviteRequest = []
        self.privilegeOfCommentOnUserProfile = []
        self.pushEnabled = []
        self.race = []
        self.reputation = []
        self.role = []
        self.securityLevel = []
        self.staffInfo = []
        self.status = []
        self.storiesCount = []
        self.strikeCount = []
        self.tagList = []
        self.twitterId = []
        self.userId = []
        self.verified = []
        self.visitPrivacy = []
        self.visitorsCount = []
        self.warningCount = []
        self.totalQuizPlayedTimes = []
        self.totalQuizHighestScore = []
        self.requestId = []
        self.message = []
        self.applicant = []
        self.avgDailySpendTimeIn7Days = []
        self.adminLogCountIn7Days = []

    @property
    def UserProfileList(self):
        for x in self.json:
            try: self.accountMembershipStatus.append(x["accountMembershipStatus"])
            except (KeyError, TypeError): self.accountMembershipStatus.append(None)
            try: self.activation.append(x["activation"])
            except (KeyError, TypeError): self.activation.append(None)
            try: self.activePublicLiveThreadId.append(x["activePublicLiveThreadId"])
            except (KeyError, TypeError): self.activePublicLiveThreadId.append(None)
            try: self.age.append(x["age"])
            except (KeyError, TypeError): self.age.append(None)
            try: self.aminoId.append(x["aminoId"])
            except (KeyError, TypeError): self.aminoId.append(None)
            try: self.aminoIdEditable.append(x["aminoIdEditable"])
            except (KeyError, TypeError): self.aminoIdEditable.append(None)
            try: self.appleId.append(x["appleID"])
            except (KeyError, TypeError): self.appleId.append(None)
            try: self.avatarFrame.append(x["avatarFrame"])
            except (KeyError, TypeError): self.avatarFrame.append(None)
            try: self.avatarFrameId.append(x["avatarFrameId"])
            except (KeyError, TypeError): self.avatarFrameId.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except (KeyError, TypeError): self.backgroundColor.append(None)
            try: self.backgroundImage.append(x["extensions"]["style"]["backgroundMediaList"][1])
            except (KeyError, TypeError, IndexError): self.backgroundImage.append(None)
            try: self.blogsCount.append(x["blogsCount"])
            except (KeyError, TypeError): self.blogsCount.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except (KeyError, TypeError): self.commentsCount.append(None)
            try: self.content.append(x["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.coverAnimation.append(x["extensions"]["coverAnimation"])
            except (KeyError, TypeError): self.coverAnimation.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.customTitles.append(x["extensions"]["customTitles"])
            except (KeyError, TypeError): self.customTitles.append(None)
            try: self.dateOfBirth.append(x["dateOfBirth"])
            except (KeyError, TypeError): self.dateOfBirth.append(None)
            try: self.defaultBubbleId.append(x["extensions"]["defaultBubbleId"])
            except (KeyError, TypeError): self.defaultBubbleId.append(None)
            try: self.disabledLevel.append(x["extensions"]["__disabledLevel__"])
            except (KeyError, TypeError): self.disabledLevel.append(None)
            try: self.disabledStatus.append(x["extensions"]["__disabledStatus__"])
            except (KeyError, TypeError): self.disabledStatus.append(None)
            try: self.disabledTime.append(x["extensions"]["__disabledTime__"])
            except (KeyError, TypeError): self.disabledTime.append(None)
            try: self.email.append(x["email"])
            except (KeyError, TypeError): self.email.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.facebookId.append(x["facebookID"])
            except (KeyError, TypeError): self.facebookId.append(None)
            try: self.fansCount.append(x["influencerInfo"]["fansCount"])
            except (KeyError, TypeError): self.fansCount.append(None)
            try: self.followersCount.append(x["membersCount"])
            except (KeyError, TypeError): self.followersCount.append(None)
            try: self.followingCount.append(x["joinedCount"])
            except (KeyError, TypeError): self.followingCount.append(None)
            try: self.followingStatus.append(x["followingStatus"])
            except (KeyError, TypeError): self.followingStatus.append(None)
            try: self.gender.append(x["gender"])
            except (KeyError, TypeError): self.gender.append(None)
            try: self.globalStrikeCount.append(x["adminInfo"]["globalStrikeCount"])
            except (KeyError, TypeError): self.globalStrikeCount.append(None)
            try: self.googleId.append(x["googleID"])
            except (KeyError, TypeError): self.googleId.append(None)
            try: self.icon.append(x["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.influencerCreatedTime.append(x["influencerInfo"]["createdTime"])
            except (KeyError, TypeError): self.influencerCreatedTime.append(None)
            try: self.influencerInfo.append(x["influencerInfo"])
            except (KeyError, TypeError): self.influencerInfo.append(None)
            try: self.influencerMonthlyFee.append(x["influencerInfo"]["monthlyFee"])
            except (KeyError, TypeError): self.influencerMonthlyFee.append(None)
            try: self.influencerPinned.append(x["influencerInfo"]["pinned"])
            except (KeyError, TypeError): self.influencerPinned.append(None)
            try: self.isGlobal.append(x["isGlobal"])
            except (KeyError, TypeError): self.isGlobal.append(None)
            try: self.isMemberOfTeamAmino.append(x["extensions"]["isMemberOfTeamAmino"])
            except (KeyError, TypeError): self.isMemberOfTeamAmino.append(None)
            try: self.isNicknameVerified.append(x["isNicknameVerified"])
            except (KeyError, TypeError): self.isNicknameVerified.append(None)
            try: self.itemsCount.append(x["itemsCount"])
            except (KeyError, TypeError): self.itemsCount.append(None)
            try: self.lastStrikeTime.append(x["adminInfo"]["lastStrikeTime"])
            except (KeyError, TypeError): self.lastStrikeTime.append(None)
            try: self.lastWarningTime.append(x["adminInfo"]["lastWarningTime"])
            except (KeyError, TypeError): self.lastWarningTime.append(None)
            try: self.level.append(x["level"])
            except (KeyError, TypeError): self.level.append(None)
            try: self.mediaList.append(x["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.membershipStatus.append(x["membershipStatus"])
            except (KeyError, TypeError): self.membershipStatus.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.mood.append(x["mood"])
            except (KeyError, TypeError): self.mood.append(None)
            try: self.moodSticker.append(x["moodSticker"])
            except (KeyError, TypeError): self.moodSticker.append(None)
            try: self.nickname.append(x["nickname"])
            except (KeyError, TypeError): self.nickname.append(None)
            try: self.notificationSubscriptionStatus.append(x["notificationSubscriptionStatus"])
            except (KeyError, TypeError): self.notificationSubscriptionStatus.append(None)
            try: self.onlineStatus.append(x["onlineStatus"])
            except (KeyError, TypeError): self.onlineStatus.append(None)
            try: self.onlineStatus2.append(x["settings"]["onlineStatus"])
            except (KeyError, TypeError): self.onlineStatus2.append(None)
            try: self.phoneNumber.append(x["phoneNumber"])
            except (KeyError, TypeError): self.phoneNumber.append(None)
            try: self.postsCount.append(x["postsCount"])
            except (KeyError, TypeError): self.postsCount.append(None)
            try: self.privilegeOfChatInviteRequest.append(x["extensions"]["privilegeOfChatInviteRequest"])
            except (KeyError, TypeError): self.privilegeOfChatInviteRequest.append(None)
            try: self.privilegeOfCommentOnUserProfile.append(x["extensions"]["privilegeOfCommentOnUserProfile"])
            except (KeyError, TypeError): self.privilegeOfCommentOnUserProfile.append(None)
            try: self.pushEnabled.append(x["pushEnabled"])
            except (KeyError, TypeError): self.pushEnabled.append(None)
            try: self.race.append(x["race"])
            except (KeyError, TypeError): self.race.append(None)
            try: self.reputation.append(x["reputation"])
            except (KeyError, TypeError): self.reputation.append(None)
            try: self.role.append(x["role"])
            except (KeyError, TypeError): self.role.append(None)
            try: self.securityLevel.append(x["securityLevel"])
            except (KeyError, TypeError): self.securityLevel.append(None)
            try: self.staffInfo.append(x["adminInfo"])
            except (KeyError, TypeError): self.staffInfo.append(None)
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.storiesCount.append(x["storiesCount"])
            except (KeyError, TypeError): self.storiesCount.append(None)
            try: self.strikeCount.append(x["adminInfo"]["strikeCount"])
            except (KeyError, TypeError): self.strikeCount.append(None)
            try: self.tagList.append(x["tagList"])
            except (KeyError, TypeError): self.tagList.append(None)
            try: self.twitterId.append(x["twitterID"])
            except (KeyError, TypeError): self.twitterId.append(None)
            try: self.userId.append(x["uid"])
            except (KeyError, TypeError): self.userId.append(None)
            try: self.verified.append(x["verified"])
            except (KeyError, TypeError): self.verified.append(None)
            try: self.visitPrivacy.append(x["visitPrivacy"])
            except (KeyError, TypeError): self.visitPrivacy.append(None)
            try: self.visitorsCount.append(x["visitorsCount"])
            except (KeyError, TypeError): self.visitorsCount.append(None)
            try: self.warningCount.append(x["adminInfo"]["warningCount"])
            except (KeyError, TypeError): self.warningCount.append(None)
            try: self.totalQuizPlayedTimes.append(x["totalQuizPlayedTimes"])
            except (KeyError, TypeError): self.totalQuizPlayedTimes.append(None)
            try: self.totalQuizHighestScore.append(x["totalQuizHighestScore"])
            except (KeyError, TypeError): self.totalQuizHighestScore.append(None)
            try: self.requestId.append(x["requestId"])
            except (KeyError, TypeError): self.requestId.append(None)
            try: self.message.append(x["message"])
            except (KeyError, TypeError): self.message.append(None)
            try: self.applicant.append(x["applicant"])
            except (KeyError, TypeError): self.applicant.append(None)
            try: self.avgDailySpendTimeIn7Days.append(x["avgDailySpendTimeIn7Days"])
            except (KeyError, TypeError): self.avgDailySpendTimeIn7Days.append(None)
            try: self.adminLogCountIn7Days.append(x["adminLogCountIn7Days"])
            except (KeyError, TypeError): self.adminLogCountIn7Days.append(None)

        return self


class FanClubList:
    def __init__(self, data):
        _profile, _targetUserProfile = [], []

        self.json = data

        for y in data:
            try: _profile.append(y["fansUserProfile"])
            except (KeyError, TypeError): _profile.append(None)
            try: _targetUserProfile.append(y["targetUserProfile"])
            except (KeyError, TypeError): _targetUserProfile.append(None)

        self.profile: UserProfileList = UserProfileList(_profile).UserProfileList
        self.targetUserProfile: UserProfileList = UserProfileList(_targetUserProfile).UserProfileList
        self.userId = []
        self.lastThankedTime = []
        self.expiredTime = []
        self.createdTime = []
        self.status = []
        self.targetUserId = []

    @property
    def FanClubList(self):
        for x in self.json:
            try: self.userId.append(x["uid"])
            except (KeyError, TypeError): self.userId.append(None)
            try: self.lastThankedTime.append(x["lastThankedTime"])
            except (KeyError, TypeError): self.lastThankedTime.append(None)
            try: self.expiredTime.append(x["expiredTime"])
            except (KeyError, TypeError): self.expiredTime.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.status.append(x["fansStatus"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.targetUserId.append(x["targetUid"])
            except (KeyError, TypeError): self.targetUserId.append(None)

        return self


class UserProfile:
    def __init__(self, data):
        self.json = data

        try: self.fanClub: FanClubList = FanClubList(data["fanClubList"]).FanClubList
        except (KeyError, TypeError): self.fanClub: FanClubList = FanClubList([])

        self.accountMembershipStatus = None
        self.activation = None
        self.activePublicLiveThreadId = None
        self.age = None
        self.aminoId = None
        self.aminoIdEditable = None
        self.appleId = None
        self.avatarFrame = None
        self.avatarFrameId = None
        self.backgroundImage = None
        self.backgroundColor = None
        self.blogsCount = None
        self.commentsCount = None
        self.content = None
        self.coverAnimation = None
        self.createdTime = None
        self.customTitles = None
        self.dateOfBirth = None
        self.defaultBubbleId = None
        self.disabledLevel = None
        self.disabledStatus = None
        self.disabledTime = None
        self.email = None
        self.extensions = None
        self.facebookId = None
        self.fansCount = None
        self.followersCount = None
        self.followingCount = None
        self.followingStatus = None
        self.gender = None
        self.globalStrikeCount = None
        self.googleId = None
        self.icon = None
        self.influencerCreatedTime = None
        self.influencerInfo = None
        self.influencerMonthlyFee = None
        self.influencerPinned = None
        self.isGlobal = None
        self.isMemberOfTeamAmino = None
        self.isNicknameVerified = None
        self.itemsCount = None
        self.lastStrikeTime = None
        self.lastWarningTime = None
        self.level = None
        self.mediaList = None
        self.membershipStatus = None
        self.modifiedTime = None
        self.mood = None
        self.moodSticker = None
        self.nickname = None
        self.notificationSubscriptionStatus = None
        self.onlineStatus = None
        self.onlineStatus2 = None
        self.phoneNumber = None
        self.postsCount = None
        self.privilegeOfChatInviteRequest = None
        self.privilegeOfCommentOnUserProfile = None
        self.pushEnabled = None
        self.race = None
        self.reputation = None
        self.role = None
        self.securityLevel = None
        self.staffInfo = None
        self.status = None
        self.storiesCount = None
        self.strikeCount = None
        self.tagList = None
        self.twitterId = None
        self.userId = None
        self.verified = None
        self.visitPrivacy = None
        self.visitorsCount = None
        self.warningCount = None
        self.totalQuizHighestScore = None
        self.totalQuizPlayedTimes = None
        self.requestId = None
        self.message = None
        self.applicant = None
        self.avgDailySpendTimeIn7Days = None
        self.adminLogCountIn7Days = None

    @property
    def UserProfile(self):
        try: self.accountMembershipStatus = self.json["accountMembershipStatus"]
        except (KeyError, TypeError): pass
        try: self.activation = self.json["activation"]
        except (KeyError, TypeError): pass
        try: self.activePublicLiveThreadId = self.json["activePublicLiveThreadId"]
        except (KeyError, TypeError): pass
        try: self.age = self.json["age"]
        except (KeyError, TypeError): pass
        try: self.aminoId = self.json["aminoId"]
        except (KeyError, TypeError): pass
        try: self.aminoIdEditable = self.json["aminoIdEditable"]
        except (KeyError, TypeError): pass
        try: self.appleId = self.json["appleID"]
        except (KeyError, TypeError): pass
        try: self.avatarFrame = self.json["avatarFrame"]
        except (KeyError, TypeError): pass
        try: self.avatarFrameId = self.json["avatarFrameId"]
        except (KeyError, TypeError): pass
        try: self.backgroundColor = self.json["extensions"]["style"]["backgroundColor"]
        except (KeyError, TypeError): pass
        try: self.backgroundImage = self.json["extensions"]["style"]["backgroundMediaList"][1]
        except (KeyError, TypeError, IndexError): pass
        try: self.blogsCount = self.json["blogsCount"]
        except (KeyError, TypeError): pass
        try: self.commentsCount = self.json["commentsCount"]
        except (KeyError, TypeError): pass
        try: self.content = self.json["content"]
        except (KeyError, TypeError): pass
        try: self.coverAnimation = self.json["extensions"]["coverAnimation"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.customTitles = self.json["extensions"]["customTitles"]
        except (KeyError, TypeError): pass
        try: self.dateOfBirth = self.json["dateOfBirth"]
        except (KeyError, TypeError): pass
        try: self.defaultBubbleId = self.json["extensions"]["defaultBubbleId"]
        except (KeyError, TypeError): pass
        try: self.disabledLevel = self.json["extensions"]["__disabledLevel__"]
        except (KeyError, TypeError): pass
        try: self.disabledStatus = self.json["extensions"]["__disabledStatus__"]
        except (KeyError, TypeError): pass
        try: self.disabledTime = self.json["extensions"]["__disabledTime__"]
        except (KeyError, TypeError): pass
        try: self.email = self.json["email"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.facebookId = self.json["facebookID"]
        except (KeyError, TypeError): pass
        try: self.fansCount = self.json["influencerInfo"]["fansCount"]
        except (KeyError, TypeError): pass
        try: self.followersCount = self.json["membersCount"]
        except (KeyError, TypeError): pass
        try: self.followingCount = self.json["joinedCount"]
        except (KeyError, TypeError): pass
        try: self.followingStatus = self.json["followingStatus"]
        except (KeyError, TypeError): pass
        try: self.gender = self.json["gender"]
        except (KeyError, TypeError): pass
        try: self.globalStrikeCount = self.json["adminInfo"]["globalStrikeCount"]
        except (KeyError, TypeError): pass
        try: self.googleId = self.json["googleID"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.influencerCreatedTime = self.json["influencerInfo"]["createdTime"]
        except (KeyError, TypeError): pass
        try: self.influencerInfo = self.json["influencerInfo"]
        except (KeyError, TypeError): pass
        try: self.influencerMonthlyFee = self.json["influencerInfo"]["monthlyFee"]
        except (KeyError, TypeError): pass
        try: self.influencerPinned = self.json["influencerInfo"]["pinned"]
        except (KeyError, TypeError): pass
        try: self.isGlobal = self.json["isGlobal"]
        except (KeyError, TypeError): pass
        try: self.isMemberOfTeamAmino = self.json["extensions"]["isMemberOfTeamAmino"]
        except (KeyError, TypeError): pass
        try: self.isNicknameVerified = self.json["isNicknameVerified"]
        except (KeyError, TypeError): pass
        try: self.itemsCount = self.json["itemsCount"]
        except (KeyError, TypeError): pass
        try: self.lastStrikeTime = self.json["adminInfo"]["lastStrikeTime"]
        except (KeyError, TypeError): pass
        try: self.lastWarningTime = self.json["adminInfo"]["lastWarningTime"]
        except (KeyError, TypeError): pass
        try: self.level = self.json["level"]
        except (KeyError, TypeError): pass
        try: self.mediaList = self.json["mediaList"]
        except (KeyError, TypeError): pass
        try: self.membershipStatus = self.json["membershipStatus"]
        except (KeyError, TypeError): pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except (KeyError, TypeError): pass
        try: self.mood = self.json["mood"]
        except (KeyError, TypeError): pass
        try: self.moodSticker = self.json["moodSticker"]
        except (KeyError, TypeError): pass
        try: self.nickname = self.json["nickname"]
        except (KeyError, TypeError): pass
        try: self.notificationSubscriptionStatus = self.json["notificationSubscriptionStatus"]
        except (KeyError, TypeError): pass
        try: self.onlineStatus = self.json["onlineStatus"]
        except (KeyError, TypeError): pass
        try: self.onlineStatus2 = self.json["settings"]["onlineStatus"]
        except (KeyError, TypeError): pass
        try: self.phoneNumber = self.json["phoneNumber"]
        except (KeyError, TypeError): pass
        try: self.postsCount = self.json["postsCount"]
        except (KeyError, TypeError): pass
        try: self.privilegeOfChatInviteRequest = self.json["extensions"]["privilegeOfChatInviteRequest"]
        except (KeyError, TypeError): pass
        try: self.privilegeOfCommentOnUserProfile = self.json["extensions"]["privilegeOfCommentOnUserProfile"]
        except (KeyError, TypeError): pass
        try: self.pushEnabled = self.json["pushEnabled"]
        except (KeyError, TypeError): pass
        try: self.race = self.json["race"]
        except (KeyError, TypeError): pass
        try: self.reputation = self.json["reputation"]
        except (KeyError, TypeError): pass
        try: self.role = self.json["role"]
        except (KeyError, TypeError): pass
        try: self.securityLevel = self.json["securityLevel"]
        except (KeyError, TypeError): pass
        try: self.staffInfo = self.json["adminInfo"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.storiesCount = self.json["storiesCount"]
        except (KeyError, TypeError): pass
        try: self.strikeCount = self.json["adminInfo"]["strikeCount"]
        except (KeyError, TypeError): pass
        try: self.tagList = self.json["tagList"]
        except (KeyError, TypeError): pass
        try: self.twitterId = self.json["twitterID"]
        except (KeyError, TypeError): pass
        try: self.userId = self.json["uid"]
        except (KeyError, TypeError): pass
        try: self.verified = self.json["verified"]
        except (KeyError, TypeError): pass
        try: self.visitPrivacy = self.json["visitPrivacy"]
        except (KeyError, TypeError): pass
        try: self.visitorsCount = self.json["visitorsCount"]
        except (KeyError, TypeError): pass
        try: self.warningCount = self.json["adminInfo"]["warningCount"]
        except (KeyError, TypeError): pass
        try: self.totalQuizHighestScore = self.json["totalQuizHighestScore"]
        except (KeyError, TypeError): pass
        try: self.totalQuizPlayedTimes = self.json["totalQuizPlayedTimes"]
        except (KeyError, TypeError): pass
        try: self.requestId = self.json["requestId"]
        except (KeyError, TypeError): pass
        try: self.message = self.json["message"]
        except (KeyError, TypeError): pass
        try: self.applicant = self.json["applicant"]
        except (KeyError, TypeError): pass
        try: self.avgDailySpendTimeIn7Days = self.json["avgDailySpendTimeIn7Days"]
        except (KeyError, TypeError): pass
        try: self.adminLogCountIn7Days = self.json["adminLogCountIn7Days"]
        except (KeyError, TypeError): pass

        return self



class StickerCollection:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except (KeyError, TypeError): self.author: UserProfile = UserProfile([])
        try: self.originalAuthor: UserProfile = UserProfile(data["extensions"]["originalAuthor"]).UserProfile
        except (KeyError, TypeError): self.originalAuthor: UserProfile = UserProfile([])
        try: self.originalCommunity: Community = Community(data["extensions"]["originalCommunity"]).Community
        except (KeyError, TypeError): self.originalCommunity: Community = Community([])

        self.status = None
        self.collectionType = None
        self.modifiedTime = None
        self.bannerUrl = None
        self.smallIcon = None
        self.stickersCount = None
        self.usedCount = None
        self.icon = None
        self.title = None
        self.collectionId = None
        self.extensions = None
        self.isActivated = None
        self.ownershipStatus = None
        self.isNew = None
        self.availableComIds = None
        self.description = None
        self.iconSourceStickerId = None
        self.restrictionInfo = None
        self.discountValue = None
        self.discountStatus = None
        self.ownerId = None
        self.ownerType = None
        self.restrictType = None
        self.restrictValue = None
        self.availableDuration = None

    @property
    def StickerCollection(self):
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.collectionType = self.json["collectionType"]
        except (KeyError, TypeError): pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except (KeyError, TypeError): pass
        try: self.bannerUrl = self.json["bannerUrl"]
        except (KeyError, TypeError): pass
        try: self.smallIcon = self.json["smallIcon"]
        except (KeyError, TypeError): pass
        try: self.stickersCount = self.json["stickersCount"]
        except (KeyError, TypeError): pass
        try: self.usedCount = self.json["usedCount"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.title = self.json["name"]
        except (KeyError, TypeError): pass
        try: self.collectionId = self.json["collectionId"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.iconSourceStickerId = self.json["extensions"]["iconSourceStickerId"]
        except (KeyError, TypeError): pass
        try: self.isActivated = self.json["isActivated"]
        except (KeyError, TypeError): pass
        try: self.ownershipStatus = self.json["ownershipStatus"]
        except (KeyError, TypeError): pass
        try: self.isNew = self.json["isNew"]
        except (KeyError, TypeError): pass
        try: self.availableComIds = self.json["availableNdcIds"]
        except (KeyError, TypeError): pass
        try: self.description = self.json["description"]
        except (KeyError, TypeError): pass
        try: self.restrictionInfo = self.json["restrictionInfo"]
        except (KeyError, TypeError): pass
        try: self.discountStatus = self.json["restrictionInfo"]["discountStatus"]
        except (KeyError, TypeError): pass
        try: self.discountValue = self.json["restrictionInfo"]["discountValue"]
        except (KeyError, TypeError): pass
        try: self.ownerId = self.json["restrictionInfo"]["ownerUid"]
        except (KeyError, TypeError): pass
        try: self.ownerType = self.json["restrictionInfo"]["ownerType"]
        except (KeyError, TypeError): pass
        try: self.restrictType = self.json["restrictionInfo"]["restrictType"]
        except (KeyError, TypeError): pass
        try: self.restrictValue = self.json["restrictionInfo"]["restrictValue"]
        except (KeyError, TypeError): pass
        try: self.availableDuration = self.json["restrictionInfo"]["availableDuration"]
        except (KeyError, TypeError): pass

        return self


class Sticker:
    def __init__(self, data):
        self.json = data

        try: self.collection: StickerCollection = StickerCollection(data["stickerCollectionSummary"]).StickerCollection
        except (KeyError, TypeError): self.collection: StickerCollection = StickerCollection([])

        self.status = None
        self.icon = None
        self.iconV2 = None
        self.name = None
        self.stickerId = None
        self.smallIcon = None
        self.smallIconV2 = None
        self.stickerCollectionId = None
        self.mediumIcon = None
        self.mediumIconV2 = None
        self.extensions = None
        self.usedCount = None
        self.createdTime = None

    @property
    def Sticker(self):
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.icon = self.json["icon"]
        except (KeyError, TypeError): pass
        try: self.iconV2 = self.json["iconV2"]
        except (KeyError, TypeError): pass
        try: self.name = self.json["name"]
        except (KeyError, TypeError): pass
        try: self.stickerId = self.json["stickerId"]
        except (KeyError, TypeError): pass
        try: self.smallIcon = self.json["smallIcon"]
        except (KeyError, TypeError): pass
        try: self.smallIconV2 = self.json["smallIconV2"]
        except (KeyError, TypeError): pass
        try: self.stickerCollectionId = self.json["stickerCollectionId"]
        except (KeyError, TypeError): pass
        try: self.mediumIcon = self.json["mediumIcon"]
        except (KeyError, TypeError): pass
        try: self.mediumIconV2 = self.json["mediumIconV2"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.usedCount = self.json["usedCount"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass

        return self


class Message:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except (KeyError, TypeError): self.author: UserProfile = UserProfile([])
        try: self.sticker: Sticker = Sticker(data["extensions"]["sticker"]).Sticker
        except (KeyError, TypeError): self.sticker: Sticker = Sticker([])

        self.content = None
        self.includedInSummary = None
        self.isHidden = None
        self.messageType = None
        self.messageId = None
        self.mediaType = None
        self.mediaValue = None
        self.chatBubbleId = None
        self.clientRefId = None
        self.chatId = None
        self.createdTime = None
        self.chatBubbleVersion = None
        self.type = None
        self.extensions = None
        self.duration = None
        self.originalStickerId = None
        self.videoDuration = None
        self.videoExtensions = None
        self.videoHeight = None
        self.videoCoverImage = None
        self.videoWidth = None
        self.mentionUserIds = None
        self.tippingCoins = None

    @property
    def Message(self):
        try: self.content = self.json["content"]
        except (KeyError, TypeError): pass
        try: self.includedInSummary = self.json["includedInSummary"]
        except (KeyError, TypeError): pass
        try: self.isHidden = self.json["isHidden"]
        except (KeyError, TypeError): pass
        try: self.messageId = self.json["messageId"]
        except (KeyError, TypeError): pass
        try: self.messageType = self.json["messageType"]
        except (KeyError, TypeError): pass
        try: self.mediaType = self.json["mediaType"]
        except (KeyError, TypeError): pass
        try: self.chatBubbleId = self.json["chatBubbleId"]
        except (KeyError, TypeError): pass
        try: self.clientRefId = self.json["clientRefId"]
        except (KeyError, TypeError): pass
        try: self.chatId = self.json["threadId"]
        except (KeyError, TypeError): pass
        try: self.createdTime = self.json["createdTime"]
        except (KeyError, TypeError): pass
        try: self.chatBubbleVersion = self.json["chatBubbleVersion"]
        except (KeyError, TypeError): pass
        try: self.type = self.json["type"]
        except (KeyError, TypeError): pass
        try: self.mediaValue = self.json["mediaValue"]
        except (KeyError, TypeError): pass
        try: self.extensions = self.json["extensions"]
        except (KeyError, TypeError): pass
        try: self.duration = self.json["extensions"]["duration"]
        except (KeyError, TypeError): pass
        try: self.videoDuration = self.json["extensions"]["videoExtensions"]["duration"]
        except (KeyError, TypeError): pass
        try: self.videoHeight = self.json["extensions"]["videoExtensions"]["height"]
        except (KeyError, TypeError): pass
        try: self.videoWidth = self.json["extensions"]["videoExtensions"]["width"]
        except (KeyError, TypeError): pass
        try: self.videoCoverImage = self.json["extensions"]["videoExtensions"]["coverImage"]
        except (KeyError, TypeError): pass
        try: self.originalStickerId = self.json["extensions"]["originalStickerId"]
        except (KeyError, TypeError): pass
        # mentions fixed by enchart
        try: self.mentionUserIds = [m["uid"] for m in self.json["extensions"]["mentionedArray"]]
        except (KeyError, TypeError): pass
        try: self.tippingCoins = self.json["extensions"]["tippingCoins"]
        except (KeyError, TypeError): pass

        return self


class Payload:
    def __init__(self, data):
        self.json = data

        self.ndcId = None
        self.chatId = None
        self.alert = None

    @property
    def Payload(self):
        try: self.ndcId = self.json["ndcId"]
        except (KeyError, TypeError): pass
        try: self.ndcId = self.json["tid"]
        except (KeyError, TypeError): pass
        try: self.alert = self.json["aps"]["alert"]
        except (KeyError, TypeError): pass

        return self


class Event:
    def __init__(self, data):
        self.json = data
        self.comId = None
        self.alertOption = None
        self.membershipStatus = None
        self.actions = None
        self.target = None
        self.params = None
        self.threadType = None
        self.id = None
        self.duration = None

        try: self.message: Message = Message(data["chatMessage"]).Message
        except (KeyError, TypeError): self.message: Message = Message([])

    @property
    def Event(self):
        try: self.comId = self.json["ndcId"]
        except (KeyError, TypeError): pass
        try: self.alertOption = self.json["alertOption"]
        except (KeyError, TypeError): pass
        try: self.membershipStatus = self.json["membershipStatus"]
        except (KeyError, TypeError): pass
        try: self.actions = self.json["actions"]
        except (KeyError, TypeError): pass
        try: self.target = self.json["target"]
        except (KeyError, TypeError): pass
        try: self.params = self.json["params"]
        except (KeyError, TypeError): pass
        try: self.threadType = self.json["params"]["threadType"]
        except (KeyError, TypeError): pass
        try: self.duration = self.json["params"]["duration"]
        except (KeyError, TypeError): pass
        try: self.id = self.json["id"]
        except (KeyError, TypeError): pass

        return self