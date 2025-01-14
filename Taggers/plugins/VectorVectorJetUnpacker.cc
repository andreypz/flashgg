// VectorVectorJetUnpacker.cc
// S. Zenz, July 2015

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/EDMException.h"

#include "flashgg/DataFormats/interface/Jet.h"

#include <stdio.h>

using namespace std;
using namespace edm;

namespace flashgg {
    class VectorVectorJetUnpacker : public EDProducer
    {

    public:
        VectorVectorJetUnpacker( const ParameterSet & );
    private:
        void produce( Event &, const EventSetup & ) override;

        EDGetTokenT<View<vector<Jet> > > jetsToken_;
        unsigned int nCollections_;
    };

    VectorVectorJetUnpacker::VectorVectorJetUnpacker( const ParameterSet &iConfig ) :
        jetsToken_( consumes<View<vector<flashgg::Jet> > >( iConfig.getParameter<InputTag>( "JetsTag" ) ) ),
        nCollections_( iConfig.getParameter<unsigned int>( "NCollections" ) )
    {
        if( nCollections_ > 9 ) {
            throw cms::Exception( "Configuration" ) << " Number of jet collections more than 1 digit long is unreasonable";
            // We never needed more than 3 in tests; 5 should be safe. 10 would be bonkers
        }
        for( unsigned int i = 0 ; i < nCollections_ ; i++ ) {
            char number[2];
            sprintf( number, "%u", i );
            produces<vector<Jet> >( number );
        }
    }

    void VectorVectorJetUnpacker::produce( Event &evt, const EventSetup & )
    {

        Handle<View<vector<flashgg::Jet> > > theJets;
        evt.getByToken( jetsToken_, theJets );

        if( theJets->size() > nCollections_ ) {
            throw cms::Exception( "Configuration" ) << " Too many collections in input vector - inconsistency with MicroAOD";
        }

        for( unsigned int i = 0 ; i < nCollections_ ; i++ ) {
            auto_ptr<vector<Jet> > result( new vector<Jet> );
            if( theJets->size() > i ) {
                for( unsigned int j = 0 ; j < theJets->at( i ).size() ; j++ ) {
                    result->push_back( theJets->at( i )[j] );
                }
            }
            char number[2];
            sprintf( number, "%u", i );
            evt.put( result, number );
        }
    }
}
typedef flashgg::VectorVectorJetUnpacker FlashggVectorVectorJetUnpacker;
DEFINE_FWK_MODULE( FlashggVectorVectorJetUnpacker );
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
